
import json
import os

def read_json(file_path):
    if not os.path.isfile(file_path):
        