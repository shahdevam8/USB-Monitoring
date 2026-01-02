import os
from core.logger import log_event

def audit_usb(path):
    """
    Track all file movements on USB device
    """
    if not os.path.exists(path):
        return
    for root, _, files in os.walk(path):
        for file in files:
            log_event(f"USB FILE ACCESS: {os.path.join(root, file)}")
