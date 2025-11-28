import git
import os

def clone_repo_to_dir(repo_url: str, target_dir: str) -> str:
    """
    Clone a public repo into target_dir and return path.
    """
    # derive folder name
    try:
        repo = git.Repo.clone_from(repo_url, target_dir, depth=1)
        return target_dir
    except Exception as e:
        raise RuntimeError(f"Failed to clone repo: {e}")
