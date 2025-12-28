# /test - Test Generation Command

Generate tests for code.

## Behavior

1. Identify testable units (functions, classes, modules)
2. Generate test cases covering:
   - Happy path
   - Edge cases
   - Error conditions
3. Use existing test patterns in the codebase
4. Include setup/teardown if needed

## Test Types

| Type | When |
|------|------|
| Unit | Isolated function/method testing |
| Integration | Multiple components working together |
| Snapshot | Output comparison (UI, serialization) |
| Property | Invariants that should always hold |

## Output Format

```python
# Tests for [module/function name]

class Test[Name]:
    def test_[happy_path](self):
        """[What this tests]"""
        ...

    def test_[edge_case](self):
        """[What this tests]"""
        ...

    def test_[error_condition](self):
        """[What this tests]"""
        ...
```

## Usage

```
/test                       # Generate tests for recent code
/test --coverage            # Focus on uncovered paths
/test --type=unit           # Unit tests only
/test --framework=pytest    # Use specific framework
```
