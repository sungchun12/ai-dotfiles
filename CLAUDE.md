# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is an **ai-dotfiles** repository - a personal knowledge base and configuration system for AI development tooling. It serves as a quick reference guide for AI workflows, tool configurations, and best practices.

## Repository Structure

```
ai-dotfiles/
├── CLAUDE.md          # This file - guidance for Claude Code
├── README.md          # Overview and quick-start guide
├── configs/           # Tool configuration files (Claude, Cursor, etc.)
├── scripts/           # Automation scripts for common workflows
├── prompts/           # Reusable prompt templates and patterns
├── docs/              # Detailed documentation and mental models
└── tests/             # pytest tests
```

## Content Guidelines

When adding to this repository:

- **Scannability first**: Use clear headings, bullet points, and code blocks
- **Decision trees**: Include mental models for choosing between options
- **Practical examples**: Every concept should have a working example
- **Quick reference format**: TL;DR sections at the top of longer documents

## Commands

```bash
# Run tests
uv run pytest tests/ -v

# Run tests with coverage
uv run pytest tests/ --cov=configs --cov-report=term-missing
```

## File Conventions

- Shell scripts: Include shebang, set -e, and descriptive comments
- Python files: Use type hints and docstrings
- Config files: Add inline comments explaining non-obvious choices
- Markdown: Use collapsible sections for lengthy content
