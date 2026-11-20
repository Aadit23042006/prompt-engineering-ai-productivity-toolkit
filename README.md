# Task 2 — Prompt Engineering & AI Productivity Toolkit

A beginner-friendly Python project demonstrating practical prompt engineering techniques and AI-powered productivity workflows. This project covers zero-shot and few-shot prompting, structured outputs, prompt design principles, AI-assisted coding, debugging, prompt evaluation, and reusable productivity tools.

## Project Overview

The **Prompt Engineering & AI Productivity Toolkit** demonstrates how to design effective prompts, organize instructions, control output formats, evaluate prompt performance, and build reusable AI productivity workflows.

The project includes a Google Colab notebook, reusable Python modules, example prompts, automated tests, and an evaluation report.

## Objectives

- Understand and implement zero-shot and few-shot prompting.
- Design prompts using roles, context, instructions, and constraints.
- Generate structured outputs using JSON.
- Implement summarization, classification, and content-generation workflows.
- Explore AI-assisted coding and debugging.
- Build reusable prompt templates.
- Evaluate prompt structure and workflow behavior using automated tests.
- Develop productivity workflows for email writing, resume improvement, coding assistance, and research.

## Project Features

### 1. Zero-Shot Prompting

Demonstrates how to instruct an AI model to complete a task without providing examples.

**Example:**

```text
Classify the sentiment of the following review as positive,
negative, or neutral.

Review: The delivery was quick and the product was excellent.

Output: positive
```

### 2. Few-Shot Prompting

Demonstrates how examples can guide the model toward a specific response pattern.

**Example:**

```text
Example 1:
Input: I love this product.
Output: positive

Example 2:
Input: It arrived broken.
Output: negative

Input: The product works as expected.
Output:
```

### 3. Structured Prompt Design

Prompts are organized using the following components:

- **Role:** Defines the assistant's expertise or behavior.
- **Context:** Provides relevant background information.
- **Instruction:** Specifies the task to perform.
- **Constraints:** Defines rules, limitations, and requirements.
- **Output Format:** Specifies the expected response structure.

### 4. Structured JSON Outputs

Demonstrates JSON response formatting and JSON parsing for structured information.

**Example:**

```json
{
  "category": "billing",
  "priority": "high",
  "summary": "Customer requests invoice correction"
}
```

### 5. Summarization

Demonstrates text summarization using concise output formats while preserving important information.

### 6. Classification

Demonstrates text classification into predefined categories, including sentiment classification.

### 7. Content Generation

Provides reusable prompt structures for generating content based on a topic, audience, tone, and format.

### 8. AI-Assisted Coding and Debugging

Includes prompt templates for:

- Understanding code.
- Identifying programming errors.
- Analyzing error messages.
- Suggesting corrected code.
- Explaining code changes.
- Recommending test cases.

### 9. Reusable Prompt Templates

Provides reusable Python prompt templates for:

- Zero-shot prompting.
- Few-shot prompting.
- Summarization.
- Classification.
- Content generation.
- Coding and debugging.
- Email drafting.
- Resume improvement.
- Research assistance.

### 10. Prompt Evaluation

Includes automated checks for:

- Prompt structure.
- Required prompt sections.
- Example inclusion.
- JSON parsing.
- Classification output validity.
- Workflow execution.

The evaluation report documents the test methodology, test cases, results, and limitations.

### 11. AI Productivity Toolkit

The toolkit demonstrates productivity-oriented prompt workflows for:

| Workflow | Description |
|---|---|
| Summarization | Condense text into concise summaries. |
| Email Assistant | Generate professional email drafts. |
| Resume Assistant | Improve resume bullet points using ATS-friendly language. |
| Coding Assistant | Assist with code analysis and debugging prompts. |
| Research Assistant | Organize research questions, findings, and limitations. |
| Content Generator | Generate content using topic, audience, tone, and format. |

## Technologies Used

- Python
- Google Colab
- Jupyter Notebook
- JSON
- Python Standard Library
- `unittest`
- Optional OpenAI API integration

## Project Structure

```text
Task2_Prompt_Engineering_AI_Productivity/
│
├── README.md
├── PROJECT_STRUCTURE.md
├── requirements.txt
├── linkedin_post.md
│
├── notebooks/
│   └── Task2_Prompt_Engineering_AI_Productivity.ipynb
│
├── src/
│   └── ai_productivity_toolkit/
│       ├── __init__.py
│       ├── prompts.py
│       ├── workflows.py
│       └── evaluation.py
│
├── examples/
│   └── prompt_examples.json
│
├── tests/
│   └── test_toolkit.py
│
└── reports/
    ├── prompt_evaluation_report.md
    └── local_test_run.txt
```

## Getting Started

### Requirements

- Python 3.9 or higher.
- Git (optional, for repository management).
- Google account for Google Colab.

### Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/prompt-engineering-ai-productivity-toolkit.git
```

Navigate to the project directory:

```bash
cd prompt-engineering-ai-productivity-toolkit
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

### Run Automated Tests

```bash
python -m unittest discover -s tests -v
```

The test suite validates prompt construction, prompt templates, JSON parsing, classification, summarization, and productivity workflow behavior.

## Google Colab

The project includes a Google Colab-ready notebook:

```text
notebooks/Task2_Prompt_Engineering_AI_Productivity.ipynb
```

To execute the notebook:

1. Open [Google Colab](https://colab.research.google.com/).
2. Select **File → Upload notebook**.
3. Upload the project notebook.
4. Select **Runtime → Run all**.
5. Review the output of each section.
6. Save a copy to Google Drive.

The notebook runs in Demo Mode without requiring an API key.

## Optional Live AI Integration

The project can be extended to use live AI model responses through an API.

Install the optional SDK:

```bash
pip install openai
```

Configure your API key securely using environment variables or Google Colab Secrets.

**Never commit API keys, credentials, or private tokens to GitHub.**

Live model usage requires a valid API key, model access, and may incur API costs.

## Testing and Evaluation

The project includes automated tests and a prompt evaluation report.

### Test Coverage

- Prompt construction and required sections.
- Zero-shot prompt generation.
- Few-shot example inclusion.
- Coding and debugging prompt construction.
- Summarization workflow.
- Classification workflow.
- JSON extraction and parsing.
- Productivity workflow templates.
- Evaluation framework execution.

### Test Results

The local automated test suite completed successfully:

```text
Ran 9 tests

OK
```

The Google Colab notebook evaluation completed successfully:

```text
Passed 8/8 checks.
```

Detailed evaluation documentation is available at:

```text
reports/prompt_evaluation_report.md
```

## Limitations

- Demo Mode uses deterministic placeholder outputs and simple keyword-based classification.
- Demo Mode does not represent actual language model inference.
- Automated tests validate functionality, structure, and output format rather than semantic reasoning quality.
- Live model responses may vary depending on the model, prompt, and configuration.
- Human evaluation is recommended for factual accuracy, relevance, completeness, and usefulness.

## Future Improvements

- Integrate live LLM APIs.
- Compare zero-shot and few-shot performance across different models.
- Add human evaluation and scoring.
- Expand prompt test datasets.
- Implement advanced JSON schema validation.
- Add an interactive web interface for the productivity toolkit.
- Track prompt evaluation results across different prompt versions.

## Deliverables

- **GitHub Repository:** Source code, documentation, examples, tests, and evaluation report.
- **Google Colab Notebook:** Runnable demonstrations of prompt engineering techniques and productivity workflows.
- **Prompt Evaluation Report:** Testing methodology, results, and limitations.
- **LinkedIn Post:** Project announcement draft.

## Author

Developed as part of **Module 02 — Prompt Engineering & AI Productivity**, demonstrating practical prompt engineering concepts and reusable AI productivity workflows.

---

**Task 2 — Prompt Engineering & AI Productivity Toolkit**
