import requests

OLLAMA_MODEL = "llama3"
OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are Nyaya — an AI Constitutional Legal Risk Assessment Engine for India.

Classify the case.
Identify relevant constitutional articles.
Determine violation severity.
Determine urgency level.
Detect red flags.

STRICT FORMAT:

Case Category: <Category>

Relevant Constitutional Articles:
- Article X – Explanation

Violation Severity: <Level>

Urgency Level: <Level>

Detected Red Flags:
- Item 1

Legal Analysis:
<Explanation>

Simple Explanation:
<Plain language>

Disclaimer:
Nyaya provides informational analysis only.
"""

def analyze_case(text):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": SYSTEM_PROMPT + "\n\nUser Input:\n" + text,
            "stream": False
        }
    )

    return response.json()["response"]