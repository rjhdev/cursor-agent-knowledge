# Cursor Agent Knowledge Base

Shared knowledge repository for Cursor cloud agents and automations. Agents read from here for project context, conventions, and lessons learned, and can update it when they discover something worth preserving.

This repo is intentionally separate from application codebases so knowledge can span projects and persist across agent runs.

## Purpose

Cursor agents start each session without memory of prior work. This repository addresses that by providing:

- **Stable context** — infrastructure, tooling, team conventions, and recurring workflows
- **Cross-project knowledge** — decisions and patterns that apply beyond a single repo
- **Agent-maintained notes** — debugging insights, gotchas, and solutions agents discover over time

See [#1](https://github.com/rjhdev/cursor-agent-knowledge/issues/1) for the original intent behind this repository.

## How agents should use this repo

1. **Read first** — Check `INDEX.md` for an overview, then open only the topic files relevant to the current task.
2. **Write when it matters** — Record durable facts, not transient session state. Prefer updating an existing topic file over creating duplicates.
3. **Keep entries concise** — Short, scannable notes beat long narratives. Link to external docs when detail lives elsewhere.
4. **Commit with context** — Use clear commit messages so humans can review what agents learned.

Avoid loading every file at once. Load the minimum context needed for the task at hand.

## Repository structure

```
README.md          # This file — orientation for humans and agents
INDEX.md           # Topic index; start here when browsing knowledge
topics/            # Knowledge organized by topic (one file per subject)
  README.md        # Describes topic naming and file conventions
```

Add new topics under `topics/` as flat Markdown files (for example `topics/deployment.md`, `topics/debugging.md`).

## What to store here

**Good fits:**

- Team conventions and coding standards
- Infrastructure and environment details agents need repeatedly
- Debugging playbooks and known failure modes
- Automation and CI/CD quirks
- Links to authoritative external documentation

**Poor fits:**

- Secrets, credentials, or private keys (never commit these)
- Large generated logs or transient debug output
- Duplicated content that already lives in another repo's docs
- Session-specific scratch notes with no long-term value

## Related Cursor features

- **Automation Memories** — Per-automation persistent notes stored outside the repo (`MEMORIES.md` by default). Use for automation-specific learnings; use this repo for shared, team-wide knowledge.
- **Skills** — Task-specific instructions in `.cursor/skills/`. Skills tell agents *how* to do something; this repo holds *what* they should know while doing it.

## Contributing

Humans and agents can both contribute. When adding knowledge:

1. Add or update a file under `topics/`
2. Update `INDEX.md` with a link and one-line description
3. Open a pull request with a descriptive title and summary

For agents triggered by automations: prefer opening a PR rather than pushing directly to `main`, unless the automation prompt explicitly allows direct commits.
