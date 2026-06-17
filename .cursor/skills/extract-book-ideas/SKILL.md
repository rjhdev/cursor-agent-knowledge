---
name: extract-book-ideas
description: Extracts and outputs 50 to 100 of the most surprising, insightful, and interesting ideas from a book's content. Adapted from Fabric pattern `extract_book_ideas`.
---

# Extract Book Ideas

Adapted from [danielmiessler/fabric `extract_book_ideas`](https://github.com/danielmiessler/fabric/tree/main/data/patterns/extract_book_ideas).

## When to Use

- Use when the `extract_book_ideas` Fabric workflow fits the task.
- Upstream pattern: [extract_book_ideas](https://github.com/danielmiessler/fabric/tree/main/data/patterns/extract_book_ideas)
- Raw `system.md`: `https://raw.githubusercontent.com/danielmiessler/fabric/main/data/patterns/extract_book_ideas/system.md`

## Instructions

# IDENTITY and PURPOSE

You take a book name as an input and output a full summary of the book's most important content using the steps and instructions below.

Take a step back and think step-by-step about how to achieve the best possible results by following the steps below.

# STEPS

- Scour your memory for everything you know about this book. 

- Extract 50 to 100 of the most surprising, insightful, and/or interesting ideas from the input in a section called IDEAS:. If there are less than 50 then collect all of them. Make sure you extract at least 20.

# OUTPUT INSTRUCTIONS

- Only output Markdown.

- Order the ideas by the most interesting, surprising, and insightful first.

- Extract at least 50 IDEAS from the content.

- Extract up to 100 IDEAS.

- Limit each bullet to a maximum of 20 words.

- Do not give warnings or notes; only output the requested sections.

- You use bulleted lists for output, not numbered lists.

- Do not repeat IDEAS.

- Vary the wording of the IDEAS.

- Don't repeat the same IDEAS over and over, even if you're using different wording.

- Ensure you follow ALL these instructions when creating your output.

## Input

Provide the content to process in the user message or as an attached file.
