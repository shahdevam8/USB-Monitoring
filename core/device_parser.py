def extract_vid_pid(device_id):
    """
    Safely extract VID/PID from DeviceID string
    Returns (vid, pid) or (None, None)
    """
    if "VID_" in device_id and "PID_" in device_id:
        try:
            vid = device_id.split("VID_")[1][:4]
            pid = device_id.split("PID_")[1][:4]
            return vid, pid
        except IndexError:
            return None, None
    return None, None
