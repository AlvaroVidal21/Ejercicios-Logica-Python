import os
import json


def read_json_fn(track):
    if not os.path.isfile(track):
        return "404 - File not found"
    else:
        with open(track, "r") as file:
            data = json.load(file)
        return data
