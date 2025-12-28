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

## Isolation

Run parallel Claude Code sessions with git worktrees. See [tools.md - Parallel Execution](tools.md#parallel-execution).

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

See [tools.md - Core Tools](tools.md#core-tools) for Logfire setup.
