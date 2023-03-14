import json

SAVES_FILENAME = "Saves.json"
HELP_FILENAME = "Help.txt"


def read_help_from_file():
    return read_text(HELP_FILENAME)


def read_saves_from_file():
    return read_json(SAVES_FILENAME)


def write_saves_to_file(saves):
    write_json(SAVES_FILENAME, saves)


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
