import json

def check_json_file(file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
            if not data:
                return False
            return True
    except FileNotFoundError:
        return False