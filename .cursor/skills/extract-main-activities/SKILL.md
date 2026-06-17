---
name: extract-main-activities
description: Extracts key events and activities from transcripts or logs, providing a summary of what happened. Adapted from Fabric pattern `extract_main_activities`.
---

# Extract Main Activities

Adapted from [danielmiessler/fabric `extract_main_activities`](https://github.com/danielmiessler/fabric/tree/main/data/patterns/extract_main_activities).

## When to Use

- Use when the `extract_main_activities` Fabric workflow fits the task.
- Upstream pattern: [extract_main_activities](https://github.com/danielmiessler/fabric/tree/main/data/patterns/extract_main_activities)
- Raw `system.md`: `https://raw.githubusercontent.com/danielmiessler/fabric/main/data/patterns/extract_main_activities/system.md`

## Instructions

# IDENTITY

# STEPS

- Fully understand the input transcript or log.
 
- Extract the key events and map them on a 24KM x 24KM virtual whiteboard.
 
- See if there is any shared context between the events and try to link them together if possible.

# OUTPUT

- Write a 16 word summary sentence of the activity.
 
- Create a list of the main events that happened, such as watching media, conversations, playing games, watching a TV show, etc.

# OUTPUT INSTRUCTIONS

- Output only in Markdown with no italics or bolding.

## Input

Provide the content to process in the user message or as an attached file.
