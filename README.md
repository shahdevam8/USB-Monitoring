# 🔐 USB Device Control & Monitoring Framework – V2

A complete **Windows USB security framework** that monitors USB devices in real time, auto-blocks unauthorized devices, audits activity, and displays everything in a live GUI dashboard.

---

## ✅ What This Project Does

- Real-time USB plug & unplug detection  
- Auto-block unauthorized USB devices  
- Allowlist & Blocklist based control  
- Live GUI dashboard with logs  
- USB activity auditing  
- Stable, clean V2 architecture  

---

## 🧰 Requirements

- Windows 10 / 11  
- Python 3.10+  
- Administrator privileges  

---

## 📦 Installation

```powershell
git clone https://github.com/shahdevam8/USB-Montoring.git
cd USB-Monitoring
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ How to Run

```powershell
python run.py
```

---

## 🖥 GUI Dashboard

- Live USB activity logs
- Allowed / Blocked status
- Auto-refreshing view

Logs stored in:
```
logs/usb_activity.log
```

---

## 🔒 USB Policy Management

### allowlist.json
```json
[""]
```

### blocklist.json
```json
[""]
```

Format: `VID:PID`

---

## ⚙ settings.json

```json
{
  "auto_block": true,
  "audit_usb_files": true,
  "log_level": "INFO"
}
```

---

## 📁 Project Structure

```
USB_Device_Control_Framework_V2/
├── run.py
├── core/
├── gui/
├── config/
├── logs/
└── data/
```

---

## 🧪 Testing

- Insert USB
- Check GUI
- Verify logs
- Modify allowlist/blocklist
- Re-test device behavior

---

## 🔐 Security Note

Always run with **Administrator privileges**.

---

## 📌 License

Open-source for educational & research use.
