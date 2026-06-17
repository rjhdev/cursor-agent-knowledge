---
name: extract-agent-knowledge
description: Distill sessions, docs, and postmortems into durable agent knowledge (world model, task algorithms, gotchas, conventions). Custom pattern for cursor-agent-knowledge repos.
---

# Extract Agent Knowledge

Custom pattern for this knowledge base. Combines the structure of Fabric's
`create_upgrade_pack` and `extract_wisdom`, retargeted for engineering and agent work.

## When to Use

- After debugging, incidents, or multi-step agent sessions worth preserving
- When converting docs, ADRs, meeting notes, or threads into `topics/` entries
- Before updating `INDEX.md` with durable team or project knowledge

## Instructions

Extract surprising, useful, and durable information from the input. Focus on facts
agents will need again — not transient session state.

### STEPS

1. Read the full input and identify the domain (project, infra, tooling, process).
2. Separate **how the world works** from **how to do tasks**.
3. Capture non-obvious failure modes and team conventions explicitly.
4. Prefer specific, testable statements over vague advice.
5. Omit secrets, credentials, and one-off scratch notes.

### OUTPUT SECTIONS

Output only Markdown with these sections:

#### SUMMARY

25-word summary of the source and what knowledge it contains.

#### WORLD MODEL UPDATES

10–25 bullets (max 16 words each): beliefs about how systems, tools, or teams actually work.
Examples: dependency behavior, env quirks, auth flows, data semantics.

#### TASK ALGORITHM UPDATES

Group bullets under practical headers (e.g., Debugging, Deployment, Code Review, Testing).
15-word bullets: procedural steps agents should follow.

#### GOTCHAS

5–15 bullets: non-obvious failures, edge cases, misleading errors, footguns.

#### CONVENTIONS

5–15 bullets: naming, file layout, PR style, testing expectations, tools the team uses.

#### REFERENCES

Links, docs, tools, repos, and files cited or implied by the input.

#### RECOMMENDATIONS

5–15 actionable bullets: what to add or update in `topics/` or project docs.

#### ONE-SENTENCE TAKEAWAY

Single 15-word sentence capturing the most important durable lesson.

### OUTPUT RULES

- Use bullet lists, not numbered lists
- Do not repeat bullets or start bullets with the same words
- Do not output warnings, disclaimers, or meta commentary
- Do not include secrets or credentials

## Input

Provide the session notes, document, log excerpt, or thread to distill.
