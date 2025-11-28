from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from tempfile import TemporaryDirectory
from app.utils.git_clone import clone_repo_to_dir
from app.analysis.complexity import compute_complexity
from app.analysis.duplication import detect_duplicates_in_dir
from app.analysis.security_scan import run_bandit_scan
from app.ai.llm_review import analyze_with_llm

import os
import shutil

router = APIRouter()

@router.post("/analyze/file")
async def analyze_file(file: UploadFile = File(...)):
    content = await file.read()
    try:
        code = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File encoding not supported.")
    complexity = compute_complexity(code)
    llm_feedback = analyze_with_llm(code, file.filename)
    return JSONResponse({
        "filename": file.filename,
        "complexity": complexity,
        "llm_feedback": llm_feedback
    })

@router.post("/analyze/repo")
async def analyze_repo(repo_url: str = Form(...)):
    # clone repo into temp dir
    with TemporaryDirectory() as tmpdir:
        repo_path = clone_repo_to_dir(repo_url, tmpdir)
        # run analysis across files
        dup = detect_duplicates_in_dir(repo_path)
        bandit_report = run_bandit_scan(repo_path)
        # optionally run LLM on important files (e.g., top N)
        summary = []
        # For demo: run LLM on first Python file found
        for root, _, files in os.walk(repo_path):
            for f in files:
                if f.endswith(".py"):
                    path = os.path.join(root, f)
                    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                        code = fh.read()
                    llm_feedback = analyze_with_llm(code, f)
                    summary.append({"file": path.replace(repo_path, ""), "feedback": llm_feedback})
                    # stop after few files to limit cost
                    if len(summary) >= 3:
                        break
            if len(summary) >= 3:
                break

        return {
            "repo": repo_url,
            "duplicates": dup,
            "security": bandit_report,
            "llm_summaries": summary
        }
