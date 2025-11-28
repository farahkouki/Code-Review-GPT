import os
from sentence_transformers import SentenceTransformer, util

MODEL = SentenceTransformer("all-MiniLM-L6-v2")

def read_files_in_dir(root_dir, extensions=(".py", ".js", ".java", ".ts")):
    files = []
    for root, _, fnames in os.walk(root_dir):
        for f in fnames:
            if f.endswith(extensions):
                path = os.path.join(root, f)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                        files.append({"path": path, "content": fh.read()})
                except Exception:
                    continue
    return files

def detect_duplicates_in_dir(root_dir, threshold=0.85):
    files = read_files_in_dir(root_dir)
    if len(files) < 2:
        return []
    contents = [f["content"] for f in files]
    embeddings = MODEL.encode(contents, convert_to_tensor=True)
    dup_pairs = []
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            score = util.cos_sim(embeddings[i], embeddings[j]).item()
            if score >= threshold:
                dup_pairs.append({
                    "file_a": files[i]["path"].replace(root_dir+"/", ""),
                    "file_b": files[j]["path"].replace(root_dir+"/", ""),
                    "score": float(score)
                })
    return dup_pairs
