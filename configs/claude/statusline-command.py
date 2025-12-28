#!/usr/bin/env python3
import json
import sys
import subprocess
import os
import re

def run_git_cmd(args, cwd=None):
    """Run a git command and return stdout, or empty string on error."""
    try:
        result = subprocess.run(
            ['git'] + args,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=1
        )
        return result.stdout.strip() if result.returncode == 0 else ''
    except (subprocess.TimeoutExpired, Exception):
        return ''

def get_git_info(current_dir):
    """Get git branch and change statistics."""
    # Check if we're in a git repo
    if not run_git_cmd(['rev-parse', '--git-dir'], cwd=current_dir):
        return ''

    # Get current branch
    branch = run_git_cmd(['branch', '--show-current'], cwd=current_dir)
    if not branch:
        return ''

    git_info = f' | 🌿 {branch}'

    # Get diff stats for tracked files
    diff_stat = run_git_cmd(['-c', 'core.filemode=false', 'diff', 'HEAD', '--shortstat'], cwd=current_dir)

    insertions = 0
    deletions = 0

    # Parse insertions and deletions from diff stat
    if diff_stat:
        ins_match = re.search(r'(\d+) insertion', diff_stat)
        del_match = re.search(r'(\d+) deletion', diff_stat)
        if ins_match:
            insertions = int(ins_match.group(1))
        if del_match:
            deletions = int(del_match.group(1))

    # Count lines in untracked files
    untracked_files = run_git_cmd(['ls-files', '--others', '--exclude-standard'], cwd=current_dir)
    if untracked_files:
        for file_path in untracked_files.split('\n'):
            if file_path:
                full_path = os.path.join(current_dir, file_path)
                try:
                    if os.path.isfile(full_path):
                        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                            insertions += sum(1 for _ in f)
                except Exception:
                    pass

    # Add change stats to output
    if insertions or deletions:
        stats = []
        if insertions:
            stats.append(f'+{insertions}')
        if deletions:
            stats.append(f'-{deletions}')
        git_info += f' ({", ".join(stats)})'

    return git_info

def main():
    # Read JSON from stdin
    try:
        data = json.load(sys.stdin)
    except Exception:
        print('[Error reading input]')
        return

    # Extract values
    model_display = data.get('model', {}).get('display_name', 'Unknown')
    current_dir = data.get('workspace', {}).get('current_dir', '')

    # Get full directory path
    dir_path = current_dir if current_dir else ''

    # Get git info
    git_info = get_git_info(current_dir) if current_dir else ''

    # Print status line
    print(f'[{model_display}] 📁 {dir_path}{git_info}')

if __name__ == '__main__':
    main()