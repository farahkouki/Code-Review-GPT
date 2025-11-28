import subprocess
import os
import json
from tempfile import NamedTemporaryFile

def run_bandit_scan(path: str):
    """
    Lance bandit (outil CLI) sur le répertoire et retourne un résumé JSON.
    """
    try:
        # bandit can output json
        process = subprocess.run(
            ["bandit", "-r", path, "-f", "json"],
            capture_output=True,
            text=True,
            check=False
        )
        if process.returncode != 0 and process.stdout.strip() == "":
            # some errors but still return stderr
            return {"error": process.stderr}
        try:
            data = json.loads(process.stdout)
            # simplifier le rapport
            issues = []
            for rep in data.get("results", []):
                issues.append({
                    "file": rep.get("filename"),
                    "line": rep.get("line_number"),
                    "test_name": rep.get("test_name"),
                    "issue_text": rep.get("issue_text"),
                    "severity": rep.get("issue_severity")
                })
            return {"issues": issues, "metrics": data.get("metrics", {})}
        except Exception:
            return {"raw": process.stdout}
    except FileNotFoundError:
        return {"error": "bandit not installed in environment; install bandit to enable security scan."}
