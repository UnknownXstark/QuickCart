import json
import os

def save_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_data(filename):
    if not os.path.exists(filename):
        return[]
    with open(filename, "r") as f:
        return json.load(f)