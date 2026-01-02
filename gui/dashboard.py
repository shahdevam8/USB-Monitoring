import tkinter as tk
from core.path_utils import get_path

def start_gui():
    root = tk.Tk()
    root.title("USB Security Dashboard")

    text = tk.Text(root, width=100, height=30)
    text.pack()

    def refresh():
        try:
            with open(get_path("logs", "usb_activity.log"), "r") as f:
                text.delete(1.0, tk.END)
                text.insert(tk.END, f.read())
        except:
            pass
        root.after(2000, refresh)

    refresh()
    root.mainloop()
