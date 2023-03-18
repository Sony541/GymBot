import json
from time import time

HELP_FILENAME = "Help.txt"
TASKS_FILENAME = "Tasks.json"
LOG_FILENAME = "Log.json"

def add_exercise(task, weight):
    o = {
        "date": time(),
        "task": task,
        "weight": weight
    }
    append_text(LOG_FILENAME, json.dumps(o))

def read_help_from_file():
    return read_text(HELP_FILENAME)


def read_tasks_from_file():
    return read_json(TASKS_FILENAME)

# Functions for JSON


def read_json(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def write_json(filename, obj):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4)


# Functions for text


def read_text(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()


def write_text(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def append_text(filename, text):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
