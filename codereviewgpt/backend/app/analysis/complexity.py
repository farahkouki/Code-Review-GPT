from radon.complexity import cc_visit
from radon.visitors import ComplexityVisitor

def compute_complexity(code: str):
    """
    Retourne une liste des fonctions/méthodes avec leur complexité.
    """
    try:
        results = cc_visit(code)
    except Exception:
        return []
    out = []
    for r in results:
        out.append({"name": r.name, "complexity": r.complexity, "lineno": r.lineno})
    return out
