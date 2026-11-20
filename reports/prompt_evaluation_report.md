# Prompt Evaluation Report

## Purpose
Evaluate the toolkit's reusable prompt construction and deterministic demo workflows against measurable requirements. This is a software/format evaluation, not a semantic benchmark of an LLM.

## Method
- Automated unit tests check prompt sections, inclusion of few-shot examples, coding/debugging context, workflow behavior, and JSON extraction.
- Notebook evaluation checks the expected response shape and allowed labels.
- Demo workflows are deterministic and deliberately labeled as placeholders/keyword heuristics.

## Test cases
| ID | Area | Check | Result |
|---|---|---|---|
| P01 | Prompt structure | Role/context/instruction/constraints/output format present | Pass |
| P02 | Zero-shot | Task instruction included | Pass |
| P03 | Few-shot | Example input/output included | Pass |
| P04 | Coding/debugging | Error and expected behavior included | Pass |
| P05 | Classification | JSON output contract included | Pass |
| W01 | Summarization | Returns text from input | Pass |
| W02 | Classification | Output label in allowed set | Pass |
| W03 | JSON | Parses valid JSON object | Pass |
| W04 | Productivity | Email/resume prompt workflows return artifacts | Pass |

## Interpretation
The included tests validate template integrity and basic deterministic behavior. They do **not** prove that a language model follows instructions, that summaries are factually complete, or that generated emails/resumes are high quality. Those should be evaluated with live model runs and human review.

## Suggested live-model scoring rubric
Score each response from 1–5 on: instruction adherence, factual grounding, completeness, clarity, format correctness, and usefulness. Record model/version, prompt, input, output, scores, and reviewer notes. Compare prompt variants on the same test inputs.
