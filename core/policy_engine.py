import json
from core.path_utils import get_path
from core.usb_blocker import block_usb
from core.logger import log_event

def load_list(file):
    path = get_path(file)
    with open(path, "r") as f:
        return json.load(f)

ALLOW = load_list("config/allowlist.json")
BLOCK = load_list("config/blocklist.json")

def evaluate_device(vid, pid):
    key = f"{vid}:{pid}"
    if key in BLOCK:
        block_usb(vid, pid)
        log_event(f"BLOCKED USB {key}")
    elif key in ALLOW:
        log_event(f"ALLOWED USB {key}")
    else:
        log_event(f"UNKNOWN USB {key}")
