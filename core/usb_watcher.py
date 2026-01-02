import pythoncom
import wmi
import time
from core.device_parser import extract_vid_pid
from core.policy_engine import evaluate_device
from core.logger import log_event

def watch_usb():
    """
    Real-time USB monitoring (thread-safe COM)
    """
    pythoncom.CoInitialize()  # COM initialization for this thread
    c = wmi.WMI()
    log_event("USB Watcher Started")

    # Watch for device change events
    watcher = c.Win32_DeviceChangeEvent.watch_for()
    try:
        while True:
            try:
                event = watcher()  # Waits for next event
                log_event("USB change detected")

                # Scan all USB hubs when a change occurs
                for usb in c.Win32_USBHub():
                    vid, pid = extract_vid_pid(usb.DeviceID)
                    if not vid:
                        continue
                    evaluate_device(vid, pid)
            except wmi.x_wmi_timed_out:
                # Optional: can ignore timeout and continue
                continue
            except Exception as e:
                log_event(f"Error in USB watcher inner loop: {e}")
                continue

            time.sleep(0.5)  # small delay to reduce CPU usage

    finally:
        pythoncom.CoUninitialize()
