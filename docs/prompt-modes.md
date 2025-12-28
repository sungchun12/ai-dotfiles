# Prompt Modes

Different prompting strategies optimized for different tasks.

## Exploration Mode

**Goal:** Discover, understand, map out unknowns.

- Open-ended questions
- Ask for multiple perspectives
- Request examples and edge cases
- Use [Quint-code](https://github.com/m0n0x41d/quint-code) for structured hypothesis building

```
"What are the different approaches to X?"
"Show me how this module connects to the rest of the system"
"What are the trade-offs between A and B?"
```

## Reasoning Mode

**Goal:** Work through a problem systematically.

**Techniques:**
- Step-by-step decomposition
- Use [Quint-code](https://github.com/m0n0x41d/quint-code) for structured hypothesis building

```
"Think through step by step how XYZ needs to be achieved"
"Break down the problem into sub-problems"
"What assumptions are we making?"
```

## Long-Term Planning Mode

**Goal:** Design systems, architect solutions.

**Techniques:**
- Be declarative: specify the outcome, not the steps
- Add measurable success criteria
- Use Claude Code's plan mode
- Name the tech stack if you have a clear vision
- Use [beads](https://github.com/steveyegge/beads) for project management

```
"Design a system that handles X. Success criteria:
- Must support 1000 concurrent users
- Response time under 200ms
- Uses PostgreSQL and Redis"
```

**Activate:** `claude --plan` or type `/plan` in session

## Role Play Mode

**Goal:** Get specialized expertise or perspective.

**Technique:** Prefill a bracketed role name to keep Claude in character:

```
[SECURITY_AUDITOR] Review this authentication flow for vulnerabilities.

[SENIOR_SRE] What would you change about this deployment pipeline?
```

**Tip:** Combine with system prompts for longer conversations.

## General Tips

| Technique | Example |
|-----------|---------|
| Force JSON output | Prefill response with `{` |
| Provide examples | Use `<example>` XML tags |
| Assign a role | Add to system prompt |
| Improve prompts | Use Claude's prompt improver |

**Resources:**
- [Anthropic prompt library](https://docs.anthropic.com/en/prompt-library)
- [Prompt engineering guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)

## Mode Selection

```
What are you trying to do?
├── Understand something → Exploration
├── Solve a problem → Reasoning
├── Build something big → Long-Term Planning
└── Get specialized advice → Role Play
```
