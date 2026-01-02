from threading import Thread
from core.usb_watcher import watch_usb
from gui.dashboard import start_gui

# Start USB watcher in background thread (daemon)
Thread(target=watch_usb, daemon=True).start()

# Launch GUI (main thread)
start_gui()
