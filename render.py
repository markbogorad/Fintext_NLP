import os
import json

def clean_notebook(path):
    with open(path, "r", encoding="utf-8") as f:
        try:
            notebook = json.load(f)
        except Exception as e:
            print(f"Failed to load {path}: {e}")
            return

    if "widgets" in notebook.get("metadata", {}):
        del notebook["metadata"]["widgets"]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(notebook, f, indent=1)
        print(f"Cleaned: {path}")
    else:
        print(f" No widget fix needed: {path}")

# Walk through all directories and fix .ipynb files
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".ipynb"):
            full_path = os.path.join(root, file)
            clean_notebook(full_path)
