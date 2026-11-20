"""Lightweight prompt checks and JSON parsing utilities."""
import json
import re

def extract_json_object(text):
    """Extract and parse the first JSON object from a response."""
    if isinstance(text, dict):
        return text
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        raise ValueError("No JSON object found")
    return json.loads(match.group(0))

def run_prompt_tests():
    from .prompts import zero_shot_prompt, few_shot_prompt, coding_debug_prompt, classification_prompt
    from .workflows import summarize_text, classify_text
    checks = []
    p = zero_shot_prompt("Summarize", "Some source", ["Keep it factual"], "3 bullets")
    checks.append(("zero-shot includes instruction", "Summarize" in p))
    p2 = few_shot_prompt("Classify sentiment", [{"input":"I like it","output":"positive"}], output_format="label")
    checks.append(("few-shot example included", "I like it" in p2 and "positive" in p2))
    p3 = coding_debug_prompt("print(1/0)", "ZeroDivisionError", "return safely")
    checks.append(("coding prompt includes error", "ZeroDivisionError" in p3))
    p4 = classification_prompt("I love this", ["positive", "negative"])
    checks.append(("classification prompt specifies JSON", "JSON" in p4))
    checks.append(("summary workflow returns text", isinstance(summarize_text("One. Two. Three."), str)))
    checks.append(("demo classifier label allowed", classify_text("great work")["label"] in {"positive","negative","neutral"}))
    checks.append(("JSON parser works", extract_json_object('{"label":"positive"}')["label"] == "positive"))
    return [{"test": name, "passed": bool(ok)} for name, ok in checks]
