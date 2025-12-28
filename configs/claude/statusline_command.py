#!/usr/bin/env python3
"""
Claude Code statusline command - displays model, directory, and git info.

Optimized for minimal latency with reduced subprocess calls and efficient parsing.
"""
import json
import sys
import subprocess
import os
from typing import Optional, Tuple


def run_git_cmd(args: list[str], cwd: Optional[str] = None) -> str:
    """Run a git command and return stdout, or empty string on error."""
    try:
        result = subprocess.run(
            ['git'] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=1
        )
        return result.stdout.strip() if result.returncode == 0 else ''
    except (subprocess.TimeoutExpired, OSError):
        return ''


def count_lines_fast(file_paths: list[str], cwd: str) -> int:
    """Count total lines in files using wc -l (10-100x faster than Python)."""
    if not file_paths:
        return 0

    # Filter to existing files and build full paths
    full_paths = []
    for fp in file_paths:
        full = os.path.join(cwd, fp)
        if os.path.isfile(full):
            full_paths.append(full)

    if not full_paths:
        return 0

    try:
        # wc -l on multiple files, grab total from last line
        result = subprocess.run(
            ['wc', '-l'] + full_paths,
            capture_output=True,
            text=True,
            timeout=1
        )
        if result.returncode != 0:
            return 0

        lines = result.stdout.strip().split('\n')
        if len(full_paths) == 1:
            # Single file: output is "  123 /path/to/file"
            return int(lines[0].split()[0])
        else:
            # Multiple files: last line is "  456 total"
            return int(lines[-1].split()[0])
    except (subprocess.TimeoutExpired, OSError, ValueError, IndexError):
        return 0


def get_git_stats(cwd: str) -> Tuple[int, int]:
    """Get insertions/deletions using git diff --numstat (avoids regex parsing)."""
    # --numstat outputs: "added<tab>deleted<tab>filename" per line
    numstat = run_git_cmd(['-c', 'core.filemode=false', 'diff', 'HEAD', '--numstat'], cwd=cwd)

    if not numstat:
        return 0, 0

    insertions = 0
    deletions = 0

    for line in numstat.split('\n'):
        parts = line.split('\t')
        if len(parts) >= 2:
            # Binary files show "-" for stats
            if parts[0] != '-':
                insertions += int(parts[0])
            if parts[1] != '-':
                deletions += int(parts[1])

    return insertions, deletions


def get_git_info(cwd: str) -> str:
    """Get git branch and change statistics with minimal subprocess calls."""
    # Single call to check repo and get branch
    branch = run_git_cmd(['rev-parse', '--abbrev-ref', 'HEAD'], cwd=cwd)
    if not branch:
        return ''

    git_info = f' | 🌿 {branch}'

    # Get diff stats (tracked file changes)
    insertions, deletions = get_git_stats(cwd)

    # Get untracked files and count their lines
    untracked = run_git_cmd(['ls-files', '--others', '--exclude-standard'], cwd=cwd)
    if untracked:
        untracked_lines = count_lines_fast(untracked.split('\n'), cwd)
        insertions += untracked_lines

    # Format stats
    if insertions or deletions:
        stats = []
        if insertions:
            stats.append(f'+{insertions}')
        if deletions:
            stats.append(f'-{deletions}')
        git_info += f' ({", ".join(stats)})'

    return git_info


def format_statusline(data: dict) -> str:
    """Format the statusline from input data."""
    model_display = data.get('model', {}).get('display_name', 'Unknown')
    current_dir = data.get('workspace', {}).get('current_dir', '')

    git_info = get_git_info(current_dir) if current_dir else ''

    return f'[{model_display}] 📁 {current_dir}{git_info}'


def main():
    """Read JSON from stdin and output formatted statusline."""
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        print('[Error reading input]')
        return 1

    print(format_statusline(data))
    return 0


if __name__ == '__main__':
    sys.exit(main())
