from Config import DB_PATH
from os.path import join


def log(text):
    with open(join(DB_PATH, "syslog.txt", "a")) as f:
        f.write(f"{text}\n")
