---
name: extract-ideas
description: Extracts and outputs all the key ideas from input, presented as 15-word bullet points in Markdown. Adapted from Fabric pattern `extract_ideas`.
---

# Extract Ideas

Adapted from [danielmiessler/fabric `extract_ideas`](https://github.com/danielmiessler/fabric/tree/main/data/patterns/extract_ideas).

## When to Use

- Use when the `extract_ideas` Fabric workflow fits the task.
- Upstream pattern: [extract_ideas](https://github.com/danielmiessler/fabric/tree/main/data/patterns/extract_ideas)
- Raw `system.md`: `https://raw.githubusercontent.com/danielmiessler/fabric/main/data/patterns/extract_ideas/system.md`

## Instructions

# IDENTITY and PURPOSE

# STEPS

3. Write that graph down on a giant virtual whiteboard in your mind.

4. Now, using that graph on the virtual whiteboard, extract all of the ideas from the content in 15-word bullet points.

# OUTPUT

- Output the FULL list of ideas from the content in a section called IDEAS

# EXAMPLE OUTPUT

IDEAS

- The purpose of life is to find meaning and fulfillment in our existence.
- Business advice is too confusing for the average person to understand and apply.
- (continued)

END EXAMPLE OUTPUT

# OUTPUT INSTRUCTIONS

- Only output Markdown.
- Do not give warnings or notes; only output the requested sections.
- Do not omit any ideas
- Do not repeat ideas
- Do not start items with the same opening words.
- Ensure you follow ALL these instructions when creating your output.

## Input

Provide the content to process in the user message or as an attached file.
