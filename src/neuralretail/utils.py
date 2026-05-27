import json
from pathlib import Path

def save_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2))