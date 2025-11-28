# models.py
# Ajoute ici des Pydantic models si tu veux valider les réponses
from pydantic import BaseModel
from typing import Any, List, Dict

class LLMFeedback(BaseModel):
    summary: str | None = None
    issues: List[str] | None = None
    suggestions: List[str] | None = None
    snippet: str | None = None
    score: int | None = None
    reason: str | None = None
