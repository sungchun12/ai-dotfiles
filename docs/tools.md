# AI Development Tool Ecosystem

Quick reference for tools in the AI-assisted development workflow.

## Core Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| [Claude Code](https://claude.ai/code) | Main agent CLI | Daily coding, refactoring, debugging |
| [Cursor](https://cursor.sh) | AI-native IDE | Real-time code changes, cmd+k quick edits |
| [Pydantic-ai](https://ai.pydantic.dev/) | Multi-agent framework | Problems requiring mixed agents + determinism |
| [Logfire](https://logfire.pydantic.dev/docs/) | Observability | Tracing agent workflows (free tier) |

## Memory & Context Tools

| Tool | Purpose | Best For |
|------|---------|----------|
| `CLAUDE.md` | Project-level context | Tech stack, conventions, architecture |
| [Beads](https://github.com/steveyegge/beads) | Task/issue tracking | Complex task dependencies |
| [Mem0](https://mem0.ai) | Per-user memory | Multi-user AI applications |

**Decision Tree:**
```
Building an AI app with multiple users?
├── Yes → Mem0 for per-user memory
└── No → Managing complex task dependencies?
    ├── Yes → Beads
    └── No → CLAUDE.md + periodic checkpoints
```

## Reasoning & Workflow Frameworks

| Framework | Focus | Use Case |
|-----------|-------|----------|
| [Quint-code](https://github.com/m0n0x41d/quint-code) | Structured reasoning | Complex planning, hypothesis building |
| [SuperClaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) | End-to-end workflow | Full development lifecycle |

**Tip:** Couple Quint-code with Claude Code's plan mode for rigorous problem decomposition.

## Parallel Execution

Run isolated Claude Code sessions with git worktrees:
- [Git worktrees docs](https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees)

```bash
# Create worktree for parallel work
git worktree add ../feature-branch feature-branch
cd ../feature-branch
claude
```

## Links

- [Claude Code docs](https://code.claude.com/docs/en/overview)
- [Beads tutorial](https://betterstack.com/community/guides/ai/beads-issue-tracker-ai-agents/)
- [Anthropic prompt library](https://docs.anthropic.com/en/prompt-library)
