#!/bin/bash
set -e

# ai-dotfiles setup script
# Creates symlinks for AI tool configurations

DOTFILES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Setting up ai-dotfiles from: $DOTFILES_DIR"

# Claude Code settings
if [ -d "$HOME/.claude" ]; then
  echo "Linking Claude Code settings..."
  ln -sf "$DOTFILES_DIR/configs/claude/settings.json" "$HOME/.claude/settings.json"

  # Link custom commands if commands directory exists
  if [ -d "$DOTFILES_DIR/configs/claude/commands" ]; then
    mkdir -p "$HOME/.claude/commands"
    for cmd in "$DOTFILES_DIR/configs/claude/commands"/*.md; do
      [ -f "$cmd" ] && ln -sf "$cmd" "$HOME/.claude/commands/$(basename "$cmd")"
    done
  fi
else
  echo "~/.claude not found - skipping Claude Code setup"
fi

echo "Done!"
