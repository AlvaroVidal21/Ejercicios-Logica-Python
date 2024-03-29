import json
import os

def read_json_fn(track):
    if not os.path(track):
        with open(track, "w") as file:
            json.dump([], file)
    
    with open(track, "r") as file:
        data = json.load(file)

    return data