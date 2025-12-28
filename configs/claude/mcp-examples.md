# MCP Server Configuration Examples

MCP (Model Context Protocol) servers extend Claude Code with additional tools.

## Configuration Location

- **Project-level:** `.mcp.json` in project root
- **Global:** `~/.claude/mcp.json`

## Example Configurations

### Quint-code (Structured Reasoning)

```json
{
  "mcpServers": {
    "quint-code": {
      "command": "uvx",
      "args": ["quint-code"]
    }
  }
}
```

Or with explicit path:

```json
{
  "mcpServers": {
    "quint-code": {
      "command": "/Users/you/.local/bin/quint-code",
      "args": ["serve"],
      "cwd": "/path/to/project",
      "env": {
        "QUINT_PROJECT_ROOT": "/path/to/project"
      }
    }
  }
}
```

### Filesystem Access

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/directory"
      ]
    }
  }
}
```

### PostgreSQL Database

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://user:pass@localhost:5432/dbname"
      ]
    }
  }
}
```

### GitHub

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<your-token>"
      }
    }
  }
}
```

### Multiple Servers

```json
{
  "mcpServers": {
    "quint-code": {
      "command": "uvx",
      "args": ["quint-code"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/data"]
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
    }
  }
}
```

## Verifying Configuration

After adding servers, restart Claude Code and check:

```bash
# In Claude Code session
/mcp
```

This shows connected MCP servers and available tools.

## Common Issues

| Issue | Fix |
|-------|-----|
| Server not found | Check `command` path, ensure binary is installed |
| Permission denied | Check file permissions, `cwd` path |
| Connection timeout | Increase timeout, check server logs |
| Tools not showing | Restart Claude Code after config change |

## Resources

- [MCP Specification](https://modelcontextprotocol.io/)
- [MCP Server Registry](https://github.com/modelcontextprotocol/servers)
