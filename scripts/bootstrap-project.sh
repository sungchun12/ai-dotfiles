#!/bin/bash
set -e

# Bootstrap a new project with ai-dotfiles configurations
#
# Usage:
#   ./bootstrap-project.sh /path/to/new/project
#   ./bootstrap-project.sh .  # Current directory
#
# What it does:
#   - Creates CLAUDE.md template
#   - Copies prompt templates to .claude/
#   - Sets up .mcp.json if quint-code is desired

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOTFILES_DIR="$(dirname "$SCRIPT_DIR")"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

usage() {
    echo "Usage: $0 <project-directory>"
    echo ""
    echo "Bootstrap a new project with Claude Code configurations."
    echo ""
    echo "Options:"
    echo "  -h, --help     Show this help message"
    echo "  --with-quint   Include quint-code MCP configuration"
    echo "  --with-beads   Initialize beads issue tracking"
    exit 1
}

# Parse arguments
WITH_QUINT=false
WITH_BEADS=false
PROJECT_DIR=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            ;;
        --with-quint)
            WITH_QUINT=true
            shift
            ;;
        --with-beads)
            WITH_BEADS=true
            shift
            ;;
        *)
            PROJECT_DIR="$1"
            shift
            ;;
    esac
done

if [[ -z "$PROJECT_DIR" ]]; then
    usage
fi

# Resolve to absolute path
PROJECT_DIR="$(cd "$PROJECT_DIR" 2>/dev/null && pwd)" || {
    echo "Creating directory: $1"
    mkdir -p "$1"
    PROJECT_DIR="$(cd "$1" && pwd)"
}

echo -e "${GREEN}Bootstrapping project: $PROJECT_DIR${NC}"

# Create CLAUDE.md if it doesn't exist
if [[ ! -f "$PROJECT_DIR/CLAUDE.md" ]]; then
    echo "Creating CLAUDE.md..."
    cat > "$PROJECT_DIR/CLAUDE.md" << 'EOF'
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

<!-- Describe your project here -->

## Commands

```bash
# Add your common commands here
# npm test
# uv run pytest
```

## Architecture

<!-- Describe key architectural decisions -->

## Conventions

<!-- List coding conventions, naming patterns, etc. -->
EOF
    echo -e "  ${GREEN}✓${NC} Created CLAUDE.md"
else
    echo -e "  ${YELLOW}⊘${NC} CLAUDE.md already exists, skipping"
fi

# Copy prompt templates
if [[ -d "$DOTFILES_DIR/prompts" ]]; then
    mkdir -p "$PROJECT_DIR/.claude/prompts"
    cp -n "$DOTFILES_DIR/prompts/system/"*.md "$PROJECT_DIR/.claude/prompts/" 2>/dev/null || true
    echo -e "  ${GREEN}✓${NC} Copied prompt templates to .claude/prompts/"
fi

# Setup quint-code if requested
if [[ "$WITH_QUINT" == true ]]; then
    if [[ ! -f "$PROJECT_DIR/.mcp.json" ]]; then
        cat > "$PROJECT_DIR/.mcp.json" << EOF
{
  "mcpServers": {
    "quint-code": {
      "command": "uvx",
      "args": ["quint-code"]
    }
  }
}
EOF
        echo -e "  ${GREEN}✓${NC} Created .mcp.json with quint-code"
    else
        echo -e "  ${YELLOW}⊘${NC} .mcp.json already exists, skipping"
    fi
fi

# Initialize beads if requested
if [[ "$WITH_BEADS" == true ]]; then
    if command -v bd &> /dev/null; then
        if [[ ! -d "$PROJECT_DIR/.beads" ]]; then
            (cd "$PROJECT_DIR" && bd init)
            echo -e "  ${GREEN}✓${NC} Initialized beads"
        else
            echo -e "  ${YELLOW}⊘${NC} .beads already exists, skipping"
        fi
    else
        echo -e "  ${YELLOW}⊘${NC} beads not installed, skipping (install: pip install beads)"
    fi
fi

echo ""
echo -e "${GREEN}Done!${NC} Next steps:"
echo "  1. Edit CLAUDE.md with your project details"
echo "  2. cd $PROJECT_DIR && claude"
