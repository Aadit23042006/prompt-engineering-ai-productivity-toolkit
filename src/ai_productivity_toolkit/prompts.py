"""Reusable prompt templates for prompt engineering practice."""

def build_prompt(role, context, instruction, constraints=None, output_format=None):
    """Compose a prompt using role, context, instruction, constraints, and output format."""
    sections = [
        f"ROLE:\n{role.strip()}",
        f"CONTEXT:\n{context.strip()}",
        f"INSTRUCTION:\n{instruction.strip()}",
    ]
    if constraints:
        if isinstance(constraints, (list, tuple)):
            constraints = "\n".join(f"- {c}" for c in constraints)
        sections.append(f"CONSTRAINTS:\n{constraints.strip()}")
    if output_format:
        sections.append(f"OUTPUT FORMAT:\n{output_format.strip()}")
    return "\n\n".join(sections)

def zero_shot_prompt(task, context="", constraints=None, output_format=None):
    return build_prompt("You are a helpful assistant.", context or "No additional context provided.", task, constraints, output_format)

def few_shot_prompt(task, examples, context="", constraints=None, output_format=None):
    examples_text = "\n\n".join(
        f"Example {i+1}\nInput: {ex['input']}\nOutput: {ex['output']}"
        for i, ex in enumerate(examples)
    )
    context_block = context.strip()
    if examples_text:
        context_block = (context_block + "\n\n" if context_block else "") + "EXAMPLES:\n" + examples_text
    return build_prompt("You are a helpful assistant that follows examples.", context_block or "No additional context provided.", task, constraints, output_format)

def summarization_prompt(text, target_length="3 bullet points", audience="general reader"):
    return build_prompt(
        "You are an accurate summarization assistant.",
        f"Source text:\n{text}",
        f"Summarize the source for a {audience}.",
        ["Preserve key facts and do not add unsupported claims.", f"Target length: {target_length}."],
        "Bulleted list"
    )

def classification_prompt(text, labels):
    return build_prompt(
        "You are a precise text classifier.",
        f"Text to classify:\n{text}\n\nAllowed labels: {', '.join(labels)}",
        "Choose exactly one label from the allowed labels.",
        ["Do not invent labels.", "If uncertain, select the closest label and briefly explain."],
        "JSON object: {\"label\": \"...\", \"reason\": \"...\"}"
    )

def generation_prompt(topic, audience, tone, format_name, constraints=None):
    return build_prompt(
        "You are a content-generation assistant.",
        f"Topic: {topic}\nAudience: {audience}",
        f"Create content on the topic in a {tone} tone.",
        constraints or ["Stay relevant to the topic.", "Avoid fabricated facts."],
        format_name
    )

def coding_debug_prompt(code, error, expected_behavior, language="Python"):
    return build_prompt(
        f"You are an experienced {language} developer and debugging assistant.",
        f"Code:\n```{language}\n{code}\n```\nError or issue:\n{error}\nExpected behavior:\n{expected_behavior}",
        "Identify the likely root cause and propose a corrected solution.",
        ["Explain the change briefly.", "Do not silently change unrelated behavior.", "If information is missing, state assumptions."],
        "1. Diagnosis\n2. Corrected code\n3. Explanation\n4. Suggested test"
    )

def email_prompt(purpose, recipient, context, tone="professional"):
    return generation_prompt(
        f"Email: {purpose}. Recipient: {recipient}. Context: {context}",
        "busy professional", tone, "Email with subject and body",
        ["Use a clear subject.", "Keep it concise.", "Do not invent details."]
    )

def resume_prompt(role, experience, achievement):
    return build_prompt(
        "You are a resume-writing assistant.",
        f"Target role: {role}\nExperience: {experience}\nAchievement or project details: {achievement}",
        "Rewrite the details into resume bullets using action verbs and measurable impact where evidence exists.",
        ["Do not fabricate metrics, skills, employers, or outcomes.", "Use ATS-friendly wording."],
        "2-4 concise bullet points"
    )

def research_prompt(question, supplied_sources, audience="student"):
    return build_prompt(
        "You are a research assistant who distinguishes evidence from uncertainty.",
        f"Question: {question}\nSupplied sources:\n{supplied_sources}",
        f"Prepare a brief for a {audience}.",
        ["Use only supplied sources for source-based claims.", "Separate facts, interpretation, and open questions.", "Do not invent citations."],
        "Overview, key findings, evidence, limitations, next steps"
    )
