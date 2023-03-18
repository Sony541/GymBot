from os.path import join
from Config import DB_PATH

def get_log_filename(user_id):
    return join(DB_PATH, f"{user_id}_Log.json")