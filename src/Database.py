import json
from time import strftime, localtime, time
from Config import DB_PATH
from Helpers import get_log_filename
import os

HELP_FILENAME = "Help.txt"
TASKS_FILENAME = os.path.join(DB_PATH, "Tasks.json")
SYSLOG_FILENAME = os.path.join(DB_PATH, "syslog.txt")


def log(text):
    with open(SYSLOG_FILENAME, "a") as f:
        f.write(str(f"{text}\n"))

def add_exercise(task, weight, user_id):
    o = {
        "user_id": user_id,
        "date": int(time()),
        "task": task,
        "weight": weight
    }
    append_text(get_log_filename(user_id), json.dumps(o))

def load_exercise(task, user_id):
    text = read_text(get_log_filename(user_id))
    if text is None:
        return "No records file"
    res = f"{task}\n"
    for row in text.split("\n"):
        if row:
            o = json.loads(row)
            if o["task"] == task:
                time = strftime('%Y-%m-%d %H:%M', localtime(o["date"]))
                res = f"{res}{time} - {o['weight']}\n"
    return res
            
def read_help_from_file():
    return read_text(HELP_FILENAME)


def read_tasks_from_file():
    return read_json(TASKS_FILENAME)

# Functions for JSON


def read_json(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        log(e)
        return None


def write_json(filename, obj):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4)


# Functions for text


def read_text(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        log(e)
        return None


def write_text(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def append_text(filename, text):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{text}\n")
