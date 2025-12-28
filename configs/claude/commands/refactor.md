# /refactor - Code Refactoring Command

Suggest and apply code improvements.

## Behavior

1. Analyze code for improvement opportunities
2. Prioritize by impact (readability, performance, maintainability)
3. Show before/after with rationale
4. Apply changes only with confirmation

## Focus Areas

| Area | Examples |
|------|----------|
| Readability | Better names, extract functions, reduce nesting |
| Performance | Algorithmic improvements, caching, batch operations |
| Maintainability | DRY violations, separation of concerns |
| Modernization | Deprecated patterns, new language features |

## Output Format

```
## Suggested Refactors

### 1. [Change title]
**Impact:** High/Medium/Low
**Reason:** [Why this helps]

Before:
[code]

After:
[code]
```

## Usage

```
/refactor                   # Analyze and suggest improvements
/refactor --apply           # Apply all suggested changes
/refactor --focus=perf      # Focus on performance only
```
