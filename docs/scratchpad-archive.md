- [Main Agent CLI Tool: Claude-Code](https://code.claude.com/docs/en/overview)
- Claude code memory codified as project management: [https://github.com/steveyegge/beads](https://github.com/steveyegge/beads)
  - [https://betterstack.com/community/guides/ai/beads-issue-tracker-ai-agents/](https://betterstack.com/community/guides/ai/beads-issue-tracker-ai-agents/)
- Structured **reasoning** framework for Claude Code: [https://github.com/m0n0x41d/quint-code](https://github.com/m0n0x41d/quint-code)
  - experiment: couple this with plan mode
  - good for complex planning through hypothesis building
- Similar to quint-code but a structured **workflow **framework: [https://github.com/SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
  - good for end to end workflow
- Main IDE: cursor
  - I like the UI/UX of seeing code changes in real time and using cmd+k for quick changes
- How do I construct a system of agents?
  - coordination
  - shared state
  - isolated sandboxes: [https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees](https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees)
  - going back to previous state
- Custom agents
  - python CLI expert
  - design engineer
  - Courtesan: the ultimate social engineer and power graph navigator
  - Target persona: IT backoffice, accountants, data engineers
- claiw: personal toolkit for common agent workflows
  - include data analyst
- multi-agent workflow framework: [pydantic-ai](https://ai.pydantic.dev/)
  - use for problems that require a mix of agents and determinism, and more autonomy beyond an ad hoc claude code session
- observability: [logfire free tier](https://logfire.pydantic.dev/docs/#sdk)

Quick Tips:
- continue the most recent conversation `claude --continue`

**Prompt Guidelines:**

After reading through anthropic’s prompt docs, it’s informing how I should think and write depending on the mode of play I’m optimizing for:
- Exploration
- Reasoning through a problem
  - make it understand my intent: step by step lists
    - “Think through step by step how XYZ needs to be achieved”
  - use quint-codes
- Long Term Planning
  - Be declarative: specific outcome 
  - Add specific and measurable success criteria
  - Put it in plan mode
    - If I have clear vision, name the tech stack
- Role play
  - **Role-play tip**: Prefilling a bracketed `[ROLE_NAME]` can remind Claude stay in character, even for longer and more complex conversations. This is especially powerful when combined with role prompting in the `system` parameter.
- General Tips
  - Use Claude prompt improver
  - Force JSON output with prefill: ‘{‘
  - Examples with xml tags <example>
  - Give it a role for system prompts
  - [Claude.md](https://Claude.md) must be solid
  - Anthropic prompt library: [https://platform.claude.com/docs/en/resources/prompt-library/library](https://platform.claude.com/docs/en/resources/prompt-library/library)
  - What mental models should I have when exploring, planning, quick hits, reviewing ,autonomous deep work? How do I manage memory?
  - The goal should be to have so much hands-on experience that this goes beyond mental models into intuitive muscle memory

Project Need Right Tool"What's the tech stack?"[CLAUDE.md](http://CLAUDE.md)"What tasks are blocked?"Beads"What does this user prefer?"Mem0

---

The Decision Tree

Are you building an AI app with multiple users?
├── Yes → Consider Mem0 for per-user memory
└── No → Are you managing complex task dependencies?
├── Yes → Consider Beads
└── No → [CLAUDE.md](http://CLAUDE.md) + weekly checkpoints

---

Bottom Line

Mem0 = infrastructure for AI applications you're building
[CLAUDE.md/Beads](http://CLAUDE.md/Beads) = context for Claude Code sessions you're running