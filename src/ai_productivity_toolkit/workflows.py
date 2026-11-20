"""Demo-mode productivity workflows; these are deterministic and not LLM outputs."""
import json
from .prompts import summarization_prompt, classification_prompt, generation_prompt, email_prompt, resume_prompt, research_prompt

def summarize_text(text, max_sentences=3):
    sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
    return ". ".join(sentences[:max_sentences]) + ("." if sentences else "")

def classify_text(text, labels=("positive", "negative", "neutral")):
    lower = text.lower()
    positive = any(w in lower for w in ("great", "good", "love", "excellent", "happy", "helpful"))
    negative = any(w in lower for w in ("bad", "poor", "hate", "broken", "disappointed", "slow"))
    label = "positive" if positive and not negative else "negative" if negative and not positive else "neutral"
    if label not in labels:
        label = labels[-1]
    return {"label": label, "reason": "Keyword-based demo classifier; use a model for nuanced interpretation."}

def generate_content(topic, audience="general audience", tone="clear", format_name="short paragraph"):
    return f"[Demo output] A {tone} {format_name} about {topic}, written for {audience}. Replace this deterministic placeholder with a model response for real content generation."

def productivity_email(purpose, recipient, context, tone="professional"):
    return {"prompt": email_prompt(purpose, recipient, context, tone),
            "demo_output": f"Subject: {purpose}\n\nHello {recipient},\n\n[Draft based on context: {context}]\n\nBest regards"}

def resume_bullets(role, experience, achievement):
    return {"prompt": resume_prompt(role, experience, achievement),
            "demo_output": [f"• Applied relevant skills to {achievement}.", f"• Contributed to work aligned with {role}; details: {experience}."]}

def research_brief(question, supplied_sources):
    return {"prompt": research_prompt(question, supplied_sources),
            "demo_output": {"overview": "Demo brief placeholder.", "evidence": "Review supplied sources manually.", "limitations": "No external research performed in demo mode."}}
