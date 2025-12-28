# /review - Code Review Command

Review the current git diff for issues, improvements, and best practices.

## Behavior

1. Run `git diff` to see staged and unstaged changes
2. Analyze for:
   - Logic errors or bugs
   - Security concerns
   - Performance issues
   - Code style consistency
3. Provide actionable feedback

## Usage

```
/review           # Review all uncommitted changes
/review --staged  # Review only staged changes
```
