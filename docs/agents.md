# Agent Architecture

Patterns and ideas for building systems of AI agents.

## Key Questions

When designing multi-agent systems:

| Concern | Questions to Answer |
|---------|---------------------|
| Coordination | How do agents communicate? Who orchestrates? |
| Shared state | What context is shared? How is it synchronized? |
| Isolation | How do agents avoid stepping on each other? |
| Recovery | How do you roll back to a previous state? |

## Isolation with Git Worktrees

Run parallel Claude Code sessions without conflicts:

```bash
# Create isolated worktree
git worktree add ../feature-a feature-a
cd ../feature-a && claude

# In another terminal
git worktree add ../feature-b feature-b
cd ../feature-b && claude
```

Each session has its own working directory and can make independent changes.

[Full docs](https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees)

## Multi-Agent Framework

For problems requiring mixed agents + determinism, beyond ad hoc Claude Code sessions:

**[Pydantic-ai](https://ai.pydantic.dev/)** - Python framework for:
- Structured agent workflows
- Type-safe tool definitions
- Mixing AI calls with deterministic code

## Custom Agent Ideas

Specialized agents for common workflows:

| Agent | Focus | Target Users |
|-------|-------|--------------|
| Python CLI Expert | CLI tooling, argparse, typer | Backend devs |
| Design Engineer | UI/UX, component architecture | Frontend devs |
| Data Analyst | SQL, pandas, visualization | Data teams |
| Courtesan | Social engineering, stakeholder navigation | PMs, leads |

**Target personas:** IT backoffice, accountants, data engineers

## Personal Toolkit: `claiw`

Ideas for a personal agent workflow toolkit:
- Data analyst agent
- Common workflow automation
- finance analyst with monarch money
- Standardized agent interfaces
- fun to share with open community

## Observability

Track agent behavior with [Logfire](https://logfire.pydantic.dev/docs/):
- Free tier available
- Traces agent calls and tool usage
- Integrates with pydantic-ai
