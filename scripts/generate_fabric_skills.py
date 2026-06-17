#!/usr/bin/env python3
"""Generate Fabric pattern catalog and Cursor skills from a local Fabric clone."""

from __future__ import annotations

import re
import textwrap
from pathlib import Path

FABRIC_PATTERNS = Path("/tmp/fabric/data/patterns")
WORKSPACE = Path(__file__).resolve().parent.parent
SKILLS_DIR = WORKSPACE / ".cursor" / "skills"
CATALOG_PATH = WORKSPACE / "topics" / "fabric-patterns.md"
EXPLANATIONS_PATH = FABRIC_PATTERNS / "pattern_explanations.md"

GITHUB_TREE = "https://github.com/danielmiessler/fabric/tree/main/data/patterns"
GITHUB_RAW = "https://raw.githubusercontent.com/danielmiessler/fabric/main/data/patterns"

# Recommended engineering / agent workflow patterns
RECOMMENDED_PATTERNS = [
    "review_code",
    "write_pull-request",
    "summarize_git_diff",
    "explain_code",
    "create_golden_rules",
    "generate_code_rules",
    "create_design_document",
    "review_design",
    "refine_design_document",
    "create_stride_threat_model",
    "ask_secure_by_design_questions",
    "analyze_terraform_plan",
    "create_prd",
    "create_user_story",
    "create_recursive_outline",
    "analyze_incident",
    "analyze_logs",
    "explain_project",
    "improve_prompt",
    "summarize_pull-requests",
    "create_git_diff_commit",
    "write_hackerone_report",
    "write_semgrep_rule",
]

# Knowledge and wisdom extraction patterns (Group A–C from research)
KNOWLEDGE_EXTRACTION_PATTERNS = [
    "extract_wisdom",
    "extract_wisdom_agents",
    "extract_wisdom_nometa",
    "extract_wisdom_with_attribution",
    "extract_wisdom_dm",
    "extract_article_wisdom",
    "extract_insights",
    "extract_insights_dm",
    "extract_alpha",
    "extract_ideas",
    "extract_recommendations",
    "extract_core_message",
    "extract_patterns",
    "create_upgrade_pack",
    "extract_instructions",
    "capture_thinkers_work",
    "extract_book_ideas",
    "extract_book_recommendations",
    "extract_main_idea",
    "extract_primary_problem",
    "extract_primary_solution",
    "extract_references",
    "extract_algorithm_update_recommendations",
    "extract_main_activities",
]

# Whole-line theatrical fluff to drop (not substring matches on real instructions).
FLUFF_LINE_PATTERNS = [
    r"think deeply about the nature and meaning of the input for \d+",
    r"\d[\d,]*\s*IQ",
    r"spend \d+ hours",
    r"fully digest the input.*\d+ hours",
    r"re-read it \d+ times",
    r"create a \d+ meter by \d+ meter whiteboard",
    r"create a virtual whiteboard in you mind",
    r"create a virtual whiteboard in your mind",
    r"capture their work on the virtual whiteboard",
]

SKIP_SECTIONS = {"EXAMPLE", "EXAMPLES"}


def pattern_to_skill_name(pattern: str) -> str:
    return pattern.replace("_", "-")


def parse_explanations() -> dict[str, str]:
    text = EXPLANATIONS_PATH.read_text(encoding="utf-8")
    descriptions: dict[str, str] = {}
    for match in re.finditer(r"^\d+\.\s+\*\*([^*]+)\*\*:\s*(.+)$", text, re.MULTILINE):
        descriptions[match.group(1).strip()] = match.group(2).strip()
    return descriptions


def list_all_patterns() -> list[str]:
    return sorted(
        p.name
        for p in FABRIC_PATTERNS.iterdir()
        if p.is_dir() and not p.name.startswith(".")
    )


def clean_instructions(body: str) -> str:
    lines: list[str] = []
    skip_until_next_heading = False

    for line in body.splitlines():
        heading = re.match(r"^#\s+(.+)$", line.strip())
        if heading:
            title = heading.group(1).strip().upper()
            if title in SKIP_SECTIONS:
                skip_until_next_heading = True
                continue
            skip_until_next_heading = False

        if skip_until_next_heading:
            continue

        if re.match(r"^#+\s*INPUT\s*:?\s*$", line.strip(), re.IGNORECASE):
            break

        lowered = line.lower()
        if any(re.search(p, lowered, re.IGNORECASE) for p in FLUFF_LINE_PATTERNS):
            continue

        lines.append(line)

    cleaned = "\n".join(lines).strip()
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def load_pattern_instructions(pattern: str) -> str:
    system_md = FABRIC_PATTERNS / pattern / "system.md"
    if not system_md.exists():
        return f"Pattern `{pattern}` has no system.md. Fetch from upstream: {GITHUB_RAW}/{pattern}/system.md"

    raw = system_md.read_text(encoding="utf-8")
    if len(raw) > 50_000:
        # Large files (e.g. extract_insights_dm) embed huge examples between sections.
        example = re.search(r"^#\s+EXAMPLE\b", raw, re.MULTILINE)
        extraction = re.search(r"^#\s+EXTRACTION INSTRUCTIONS", raw, re.MULTILINE)
        if example and extraction and example.start() < extraction.start():
            raw = raw[: example.start()] + raw[extraction.start() :]
        elif len(raw) > 120_000:
            raw = raw[:8000] + "\n\n[Truncated: see upstream system.md for full pattern.]"

    return clean_instructions(raw)


def title_from_pattern(pattern: str) -> str:
    return pattern.replace("_", " ").replace("-", " ").title()


def build_skill(pattern: str, description: str) -> str:
    skill_name = pattern_to_skill_name(pattern)
    instructions = load_pattern_instructions(pattern)
    desc = description or f"Fabric pattern {pattern} adapted for Cursor agents."

    when_to_use = (
        f"- Use when the `{pattern}` Fabric workflow fits the task.\n"
        f"- Upstream pattern: [{pattern}]({GITHUB_TREE}/{pattern})\n"
        f"- Raw `system.md`: `{GITHUB_RAW}/{pattern}/system.md`"
    )

    return (
        f"---\n"
        f"name: {skill_name}\n"
        f"description: {desc} Adapted from Fabric pattern `{pattern}`.\n"
        f"---\n\n"
        f"# {title_from_pattern(pattern)}\n\n"
        f"Adapted from [danielmiessler/fabric `{pattern}`]({GITHUB_TREE}/{pattern}).\n\n"
        f"## When to Use\n\n"
        f"{when_to_use}\n\n"
        f"## Instructions\n\n"
        f"{instructions}\n\n"
        f"## Input\n\n"
        f"Provide the content to process in the user message or as an attached file.\n"
    )


def build_catalog(all_patterns: list[str], descriptions: dict[str, str]) -> str:
    skill_patterns = sorted(set(RECOMMENDED_PATTERNS + KNOWLEDGE_EXTRACTION_PATTERNS))
    skill_set = set(skill_patterns)

    lines = [
        "# Fabric Pattern Catalog",
        "",
        "Reference catalog for [danielmiessler/fabric](https://github.com/danielmiessler/fabric) "
        "prompt patterns. Agents can fetch any pattern on demand without loading all skills.",
        "",
        "## How to use this catalog",
        "",
        "1. Find a pattern name below that matches the task.",
        "2. Fetch the upstream prompt:",
        "   - Browse: `https://github.com/danielmiessler/fabric/tree/main/data/patterns/<pattern_name>`",
        "   - Raw: `https://raw.githubusercontent.com/danielmiessler/fabric/main/data/patterns/<pattern_name>/system.md`",
        "3. If a local skill exists under `.cursor/skills/`, prefer that skill first.",
        "",
        f"**Total patterns:** {len(all_patterns)}  ",
        f"**Local skills installed:** {len(skill_patterns) + 1} (includes `extract-agent-knowledge`)  ",
        "",
        "## Patterns with local Cursor skills",
        "",
        "| Pattern | Skill | Description |",
        "|---------|-------|-------------|",
    ]

    lines.append(
        "| extract-agent-knowledge | [extract-agent-knowledge](../.cursor/skills/extract-agent-knowledge/SKILL.md) "
        "| Custom merge of `create_upgrade_pack` + `extract_wisdom` for agent knowledge bases |"
    )

    for pattern in skill_patterns:
        skill = pattern_to_skill_name(pattern)
        desc = descriptions.get(pattern, "—")
        if len(desc) > 120:
            desc = desc[:117] + "..."
        lines.append(
            f"| {pattern} | [{skill}](../.cursor/skills/{skill}/SKILL.md) | {desc} |"
        )

    lines.extend(
        [
            "",
            "## All patterns (A–Z)",
            "",
            "| Pattern | Description | Upstream |",
            "|---------|-------------|----------|",
        ]
    )

    for pattern in all_patterns:
        desc = descriptions.get(pattern, "—")
        if len(desc) > 100:
            desc = desc[:97] + "..."
        tree = f"{GITHUB_TREE}/{pattern}"
        lines.append(f"| `{pattern}` | {desc} | [system.md]({GITHUB_RAW}/{pattern}/system.md) |")

    lines.extend(
        [
            "",
            "## Categories (quick lookup)",
            "",
            "### Knowledge extraction",
            "",
            ", ".join(f"`{p}`" for p in KNOWLEDGE_EXTRACTION_PATTERNS),
            "",
            "### Engineering and agent workflow",
            "",
            ", ".join(f"`{p}`" for p in RECOMMENDED_PATTERNS),
            "",
            "## Maintenance",
            "",
            "Regenerate skills and this catalog after updating the Fabric clone:",
            "",
            "```bash",
            "git clone --depth 1 https://github.com/danielmiessler/fabric.git /tmp/fabric",
            "python3 scripts/generate_fabric_skills.py",
            "```",
            "",
        ]
    )

    return "\n".join(lines) + "\n"


def write_skill(pattern: str, descriptions: dict[str, str]) -> None:
    skill_name = pattern_to_skill_name(pattern)
    skill_dir = SKILLS_DIR / skill_name
    skill_dir.mkdir(parents=True, exist_ok=True)
    description = descriptions.get(pattern, "")
    (skill_dir / "SKILL.md").write_text(build_skill(pattern, description), encoding="utf-8")


def write_extract_agent_knowledge() -> None:
    content = textwrap.dedent(
        """\
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
        """
    )
    skill_dir = SKILLS_DIR / "extract-agent-knowledge"
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")


def main() -> None:
    if not FABRIC_PATTERNS.is_dir():
        raise SystemExit("Clone Fabric to /tmp/fabric first.")

    descriptions = parse_explanations()
    all_patterns = list_all_patterns()

    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    patterns_to_skill = sorted(set(RECOMMENDED_PATTERNS + KNOWLEDGE_EXTRACTION_PATTERNS))
    for pattern in patterns_to_skill:
        if pattern not in all_patterns:
            print(f"warning: pattern not found: {pattern}")
            continue
        write_skill(pattern, descriptions)

    write_extract_agent_knowledge()
    CATALOG_PATH.write_text(build_catalog(all_patterns, descriptions), encoding="utf-8")

    print(f"Wrote catalog: {CATALOG_PATH}")
    print(f"Wrote {len(patterns_to_skill) + 1} skills to {SKILLS_DIR}")


if __name__ == "__main__":
    main()
