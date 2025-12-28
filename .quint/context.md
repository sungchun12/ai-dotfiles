# Bounded Context

## Vocabulary

- **Statusline**: Custom CLI status display showing model, directory, and git info.
- **MCP**: Model Context Protocol - tool integration system for Claude Code.

## Invariants

Python files use type hints and docstrings. Shell scripts include shebang and set -e. Use uv for Python dependency management. Tests use pytest. Documentation prioritizes scannability with clear headings and bullet points. Config files include inline comments explaining non-obvious choices.
