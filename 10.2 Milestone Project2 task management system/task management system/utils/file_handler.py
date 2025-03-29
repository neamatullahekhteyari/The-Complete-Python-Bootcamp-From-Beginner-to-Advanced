import json

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump([obj.__dict__ for obj in data], file, indent=4)

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
