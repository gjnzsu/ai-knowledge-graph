#!/bin/bash
# Quick skill usage logger
# Usage: ./log-skill.sh drawio

SKILL_NAME="${1:-unknown}"
LOG_FILE="$HOME/.claude/skill-usage/usage.jsonl"

echo "{\"timestamp\":\"$(date -Iseconds)\",\"skill\":\"$SKILL_NAME\"}" >> "$LOG_FILE"
echo "✓ Logged: $SKILL_NAME"
