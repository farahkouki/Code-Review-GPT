import os
import json
import openai
from app.config import OPENAI_API_KEY  # Assure-toi que le chemin est correct

# Assigner la clé API OpenAI
openai.api_key = OPENAI_API_KEY

PROMPT_TEMPLATE = """
You are a senior software engineer and code reviewer.
Given the file name: {filename}
And the code delimited by triple backticks, deliver:

1) A short summary (2-3 lines).
2) Top 5 issues (bugs, bad practices, edge cases).
3) Top 5 suggestions for refactoring or improvements.
4) If possible, give a short improved snippet or pseudocode.
5) A concise overall score (0-100) and one-line reason.

Format your answer as JSON with keys: summary, issues, suggestions, snippet, score, reason.
Code:
```{code}``` 
"""

def analyze_with_llm(code: str, filename: str):
    """
    Appelle l'API OpenAI pour obtenir un code review. Retourne un dict.
    """
    if not OPENAI_API_KEY:
        return {
            "warning": "OPENAI_API_KEY not set; LLM review skipped. Set OPENAI_API_KEY to enable.",
            "summary": "",
        }

    prompt = PROMPT_TEMPLATE.format(filename=filename, code=code[:20000])  # limite la taille

    try:
        # Nouvelle syntaxe OpenAI >=1.0.0
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # changé de gpt-4 à gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800,
        )

        # Récupérer le texte renvoyé
        text = response.choices[0].message.get("content", "") if response.choices else ""

        # Tenter de parser JSON
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"raw": text}

    except Exception as e:
        return {"error": str(e)}
