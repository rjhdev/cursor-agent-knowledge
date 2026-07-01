# AGENTS.md

## Cursor Cloud specific instructions

This repository is a **knowledge base**, not a deployable application. It is mostly
Markdown (`README.md`, `INDEX.md`, `topics/*.md`, `.cursor/skills/**/SKILL.md`).
There are no servers, databases, package manifests, or lockfiles to run or install.

### Tooling

- The only executable code is `scripts/generate_fabric_skills.py`.
- It uses the **Python 3 standard library only** — there is nothing to `pip install`.
- No lint or automated test suite is configured in this repo.

### Running the only code path (regenerate skills + catalog)

The generator reads a local [Fabric](https://github.com/danielmiessler/fabric) clone
and rewrites `.cursor/skills/**/SKILL.md` and `topics/fabric-patterns.md`.

```bash
git clone --depth 1 https://github.com/danielmiessler/fabric.git /tmp/fabric
python3 scripts/generate_fabric_skills.py
```

Gotchas:

- The script **hard-requires** the Fabric clone at `/tmp/fabric` and exits with
  `Clone Fabric to /tmp/fabric first.` if it is missing. `/tmp` is ephemeral, so the
  clone must be re-run each session before regenerating — this is why it is NOT in the
  startup update script (it is a network step, not a dependency install).
- Output is **deterministic**: a correct run against an up-to-date Fabric clone leaves
  the working tree clean (`git status` shows no changes). Use a clean `git status` after
  running as the verification that the generator works.
- Pattern counts can drift as upstream Fabric changes; if `INDEX.md`/catalog totals
  differ after regenerating, that reflects upstream Fabric, not a bug.
