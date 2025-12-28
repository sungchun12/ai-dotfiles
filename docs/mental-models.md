# Mental Models for AI-Assisted Development

## When to Use AI Coding Assistants

| Task | AI Helpfulness | Notes |
|------|----------------|-------|
| Boilerplate generation | High | Repetitive patterns, CRUD, tests |
| Code review | High | Fresh perspective, catches common issues |
| Debugging | Medium-High | Good at systematic investigation |
| Architecture decisions | Medium | Good for options, you decide |
| Novel algorithms | Low-Medium | Better to understand deeply yourself |

## Prompt Engineering Basics

**Be specific about context:**
```
Bad:  "Fix this bug"
Good: "This function should return sorted users but returns them unsorted.
       The input is an array of User objects with a 'createdAt' field."
```

**State constraints:**
```
Bad:  "Make this faster"
Good: "Optimize this query. Must stay under 100ms. Can't change the schema."
```

**Request format:**
```
Bad:  "Explain this code"
Good: "Explain this code in 2-3 sentences. Focus on the business logic, not syntax."
```

## When to Stop and Think

Pause AI assistance when:
- You don't understand the generated code
- The solution feels over-engineered
- You're copy-pasting without reading
- The AI is going in circles

## Effective Feedback Loop

1. Clear request → 2. Review output → 3. Refine or accept → 4. Verify works
