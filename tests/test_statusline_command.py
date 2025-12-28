"""Tests for statusline-command.py"""
import json
import subprocess
import sys
from io import StringIO
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'configs' / 'claude'))

from statusline_command import (
    run_git_cmd,
    count_lines_fast,
    get_git_stats,
    get_git_info,
    format_statusline,
    main,
)


# --- Fixtures ---

@pytest.fixture
def git_repo(tmp_path):
    """Create a temporary git repository for testing."""
    subprocess.run(['git', 'init'], cwd=tmp_path, capture_output=True)
    subprocess.run(
        ['git', 'config', 'user.email', 'test@test.com'],
        cwd=tmp_path, capture_output=True
    )
    subprocess.run(
        ['git', 'config', 'user.name', 'Test'],
        cwd=tmp_path, capture_output=True
    )
    return tmp_path


@pytest.fixture
def git_repo_with_commit(git_repo):
    """Git repo with an initial commit."""
    readme = git_repo / 'README.md'
    readme.write_text('# Test\n')
    subprocess.run(['git', 'add', '.'], cwd=git_repo, capture_output=True)
    subprocess.run(
        ['git', 'commit', '-m', 'Initial commit'],
        cwd=git_repo, capture_output=True
    )
    return git_repo


# --- run_git_cmd tests ---

class TestRunGitCmd:
    def test_returns_stdout_on_success(self, git_repo):
        result = run_git_cmd(['rev-parse', '--git-dir'], cwd=str(git_repo))
        assert result == '.git'

    def test_returns_empty_on_failure(self, tmp_path):
        # Not a git repo
        result = run_git_cmd(['rev-parse', '--git-dir'], cwd=str(tmp_path))
        assert result == ''

    def test_returns_empty_on_timeout(self):
        with patch('subprocess.run', side_effect=subprocess.TimeoutExpired('git', 1)):
            result = run_git_cmd(['status'])
            assert result == ''

    def test_returns_empty_on_oserror(self):
        with patch('subprocess.run', side_effect=OSError('No git')):
            result = run_git_cmd(['status'])
            assert result == ''


# --- count_lines_fast tests ---

class TestCountLinesFast:
    def test_empty_list_returns_zero(self, tmp_path):
        assert count_lines_fast([], str(tmp_path)) == 0

    def test_counts_single_file(self, tmp_path):
        f = tmp_path / 'test.txt'
        f.write_text('line1\nline2\nline3\n')
        result = count_lines_fast(['test.txt'], str(tmp_path))
        assert result == 3

    def test_counts_multiple_files(self, tmp_path):
        (tmp_path / 'a.txt').write_text('1\n2\n')
        (tmp_path / 'b.txt').write_text('1\n2\n3\n')
        result = count_lines_fast(['a.txt', 'b.txt'], str(tmp_path))
        assert result == 5

    def test_ignores_nonexistent_files(self, tmp_path):
        (tmp_path / 'exists.txt').write_text('line\n')
        result = count_lines_fast(['exists.txt', 'missing.txt'], str(tmp_path))
        assert result == 1

    def test_all_missing_returns_zero(self, tmp_path):
        result = count_lines_fast(['missing.txt'], str(tmp_path))
        assert result == 0

    def test_handles_wc_timeout(self, tmp_path):
        (tmp_path / 'test.txt').write_text('line\n')
        with patch('subprocess.run', side_effect=subprocess.TimeoutExpired('wc', 1)):
            result = count_lines_fast(['test.txt'], str(tmp_path))
            assert result == 0


# --- get_git_stats tests ---

class TestGetGitStats:
    def test_no_changes_returns_zeros(self, git_repo_with_commit):
        insertions, deletions = get_git_stats(str(git_repo_with_commit))
        assert insertions == 0
        assert deletions == 0

    def test_tracks_insertions(self, git_repo_with_commit):
        f = git_repo_with_commit / 'new.txt'
        f.write_text('line1\nline2\n')
        subprocess.run(['git', 'add', 'new.txt'], cwd=git_repo_with_commit, capture_output=True)

        insertions, deletions = get_git_stats(str(git_repo_with_commit))
        assert insertions == 2
        assert deletions == 0

    def test_tracks_deletions(self, git_repo_with_commit):
        readme = git_repo_with_commit / 'README.md'
        readme.write_text('')  # Remove the line

        insertions, deletions = get_git_stats(str(git_repo_with_commit))
        assert insertions == 0
        assert deletions == 1

    def test_tracks_both(self, git_repo_with_commit):
        readme = git_repo_with_commit / 'README.md'
        readme.write_text('New line 1\nNew line 2\n')  # Replace 1 line with 2

        insertions, deletions = get_git_stats(str(git_repo_with_commit))
        assert insertions == 2
        assert deletions == 1

    def test_handles_binary_files(self, git_repo_with_commit):
        # Simulate binary file diff output (shows "-" for stats)
        with patch('statusline_command.run_git_cmd', return_value='10\t5\tfile.txt\n-\t-\tbinary.bin'):
            insertions, deletions = get_git_stats(str(git_repo_with_commit))
            assert insertions == 10
            assert deletions == 5


# --- get_git_info tests ---

class TestGetGitInfo:
    def test_not_a_repo_returns_empty(self, tmp_path):
        result = get_git_info(str(tmp_path))
        assert result == ''

    def test_returns_branch_name(self, git_repo_with_commit):
        result = get_git_info(str(git_repo_with_commit))
        assert '🌿 main' in result or '🌿 master' in result

    def test_includes_stats_with_changes(self, git_repo_with_commit):
        f = git_repo_with_commit / 'new.txt'
        f.write_text('line1\nline2\n')
        subprocess.run(['git', 'add', 'new.txt'], cwd=git_repo_with_commit, capture_output=True)

        result = get_git_info(str(git_repo_with_commit))
        assert '+2' in result

    def test_includes_untracked_files(self, git_repo_with_commit):
        # Create untracked file
        f = git_repo_with_commit / 'untracked.txt'
        f.write_text('a\nb\nc\n')

        result = get_git_info(str(git_repo_with_commit))
        assert '+3' in result

    def test_combines_tracked_and_untracked(self, git_repo_with_commit):
        # Tracked change
        readme = git_repo_with_commit / 'README.md'
        readme.write_text('# Test\nNew line\n')  # +1 line

        # Untracked file
        (git_repo_with_commit / 'new.txt').write_text('a\nb\n')  # +2 lines

        result = get_git_info(str(git_repo_with_commit))
        assert '+3' in result  # 1 tracked + 2 untracked


# --- format_statusline tests ---

class TestFormatStatusline:
    def test_formats_model_and_dir(self):
        data = {
            'model': {'display_name': 'Claude 3.5'},
            'workspace': {'current_dir': '/home/user/project'}
        }

        with patch('statusline_command.get_git_info', return_value=''):
            result = format_statusline(data)

        assert '[Claude 3.5]' in result
        assert '📁 /home/user/project' in result

    def test_handles_missing_model(self):
        data = {'workspace': {'current_dir': '/tmp'}}

        with patch('statusline_command.get_git_info', return_value=''):
            result = format_statusline(data)

        assert '[Unknown]' in result

    def test_handles_empty_workspace(self):
        data = {'model': {'display_name': 'Claude'}}
        result = format_statusline(data)
        assert '[Claude]' in result
        assert '📁 ' in result

    def test_includes_git_info(self):
        data = {
            'model': {'display_name': 'Claude'},
            'workspace': {'current_dir': '/repo'}
        }

        with patch('statusline_command.get_git_info', return_value=' | 🌿 main (+5)'):
            result = format_statusline(data)

        assert '🌿 main' in result
        assert '+5' in result


# --- main tests ---

class TestMain:
    def test_reads_json_and_outputs(self, capsys):
        input_data = json.dumps({
            'model': {'display_name': 'Claude'},
            'workspace': {'current_dir': '/tmp'}
        })

        with patch('sys.stdin', StringIO(input_data)):
            with patch('statusline_command.get_git_info', return_value=''):
                exit_code = main()

        captured = capsys.readouterr()
        assert '[Claude]' in captured.out
        assert exit_code == 0

    def test_handles_invalid_json(self, capsys):
        with patch('sys.stdin', StringIO('not json')):
            exit_code = main()

        captured = capsys.readouterr()
        assert 'Error' in captured.out
        assert exit_code == 1

    def test_handles_empty_input(self, capsys):
        with patch('sys.stdin', StringIO('')):
            exit_code = main()

        captured = capsys.readouterr()
        assert 'Error' in captured.out
        assert exit_code == 1


# --- Integration tests ---

class TestIntegration:
    """End-to-end tests with real git repos."""

    def test_full_workflow(self, git_repo_with_commit, capsys):
        # Add some changes
        (git_repo_with_commit / 'file.txt').write_text('content\n')

        input_data = json.dumps({
            'model': {'display_name': 'Opus 4'},
            'workspace': {'current_dir': str(git_repo_with_commit)}
        })

        with patch('sys.stdin', StringIO(input_data)):
            exit_code = main()

        captured = capsys.readouterr()
        assert exit_code == 0
        assert '[Opus 4]' in captured.out
        assert '🌿' in captured.out
        assert '+1' in captured.out

    def test_performance_many_untracked_files(self, git_repo_with_commit):
        """Verify we handle many files efficiently."""
        # Create 100 small files
        for i in range(100):
            (git_repo_with_commit / f'file{i}.txt').write_text(f'line{i}\n')

        import time
        start = time.perf_counter()
        result = get_git_info(str(git_repo_with_commit))
        elapsed = time.perf_counter() - start

        assert '+100' in result
        assert elapsed < 1.0, f"Took too long: {elapsed:.2f}s"
