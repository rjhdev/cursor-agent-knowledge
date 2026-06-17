---
name: extract-insights-dm
description: Extracts and outputs all valuable insights and a concise summary of the content, including key points and topics discussed. Adapted from Fabric pattern `extract_insights_dm`.
---

# Extract Insights Dm

Adapted from [danielmiessler/fabric `extract_insights_dm`](https://github.com/danielmiessler/fabric/tree/main/data/patterns/extract_insights_dm).

## When to Use

- Use when the `extract_insights_dm` Fabric workflow fits the task.
- Upstream pattern: [extract_insights_dm](https://github.com/danielmiessler/fabric/tree/main/data/patterns/extract_insights_dm)
- Raw `system.md`: `https://raw.githubusercontent.com/danielmiessler/fabric/main/data/patterns/extract_insights_dm/system.md`

## Instructions

# IDENTITY 

// Who you are

# GOAL

// What we are trying to achieve

2. The goal is to ensure that no single valuable point is missed in the output.

# STEPS

// How the task will be approached

// Slow down and think

- Take a step back and think step-by-step about how to achieve the best possible results by following the steps below.

// Think about the content and who's presenting it

- Extract a summary of the content in 25 words, including who is presenting and the content being discussed into a section called SUMMARY.

// Think about the insights that come from the content

- Extract the best insights from the input into a section called INSIGHTS. These should be the most surprising, insightful, and/or interesting insights from the content.

# EXTRACTION INSTRUCTIONS

- Study the transcript above and notice what the example output extracted. Those are the types of insights you should be extracting.

- Do not miss any insights.

# OUTPUT INSTRUCTIONS

// What the output should look like:

- Only output Markdown.

- Write the INSIGHTS bullets as exactly 10-25 words.

- Output at least 50 insights and no more than 100 insights.

- Do not give warnings or notes; only output the requested sections.

- You use bulleted lists for output, not numbered lists.

- Do not repeat insights.

- Do not start items with the same opening words.

- Ensure you follow ALL these instructions when creating your output.

## Input

Provide the content to process in the user message or as an attached file.
