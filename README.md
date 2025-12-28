# ai-dotfiles

Personal configuration and knowledge base for AI development tooling.

## Quick Start

```bash
# Clone to your home directory
git clone https://github.com/YOUR_USERNAME/ai-dotfiles.git ~/ai-dotfiles

# Symlink Claude Code settings (optional)
ln -sf ~/ai-dotfiles/configs/claude/settings.json ~/.claude/settings.json
```

## What's Here

| Directory | Purpose |
|-----------|---------|
| `configs/` | Tool configurations (Claude, Cursor, etc.) |
| `scripts/` | Automation for common AI workflows |
| `prompts/` | Reusable prompt templates |
| `docs/` | Mental models and detailed guides |

## Key Files

- [`configs/claude/settings.json`](configs/claude/settings.json) - Claude Code preferences
- [`configs/claude/commands/`](configs/claude/commands/) - Custom slash commands
- [`prompts/system/`](prompts/system/) - System prompt templates
- [`scripts/setup.sh`](scripts/setup.sh) - One-time setup script

## Usage Patterns

**Find a prompt template:**
```bash
ls prompts/
cat prompts/code-review.md
```

**Apply a configuration:**
```bash
cp configs/claude/settings.json ~/.claude/settings.json
```

**Run a workflow script:**
```bash
./scripts/new-project.sh my-project
```

## Quick Tips

```bash
# Continue most recent conversation
claude --continue

# Start in plan mode
claude --plan

# Resume specific session
claude --resume
```

## Documentation

- [`docs/tools.md`](docs/tools.md) - Tool ecosystem and when to use each
- [`docs/prompt-modes.md`](docs/prompt-modes.md) - Prompting strategies by mode
- [`docs/agents.md`](docs/agents.md) - Multi-agent patterns and ideas
- [`docs/mental-models.md`](docs/mental-models.md) - General AI-assisted dev guidance

## Adding Content

Keep entries scannable:
- Start with the "what" and "why"
- Include working examples
- Add TL;DR for longer docs

---
