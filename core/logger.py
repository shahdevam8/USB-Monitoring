from datetime import datetime
from core.path_utils import get_path

LOG_FILE = get_path("logs", "usb_activity.log")

def log_event(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")
