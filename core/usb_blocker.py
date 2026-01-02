import subprocess

def block_usb(vid, pid):
    """
    Auto-block USB device using Windows devcon/pnputil
    Admin rights required
    """
    try:
        cmd = f'pnputil /disable-device "USB\\VID_{vid}&PID_{pid}"'
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL)
    except Exception as e:
        print(f"Failed to block USB {vid}:{pid} -> {e}")
