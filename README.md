USB_Device_Control_Framework_V2/
│
├── run.py
├── requirements.txt
├── README.md
│
├── config/
│   ├── allowlist.json
│   ├── blocklist.json
│   └── settings.json
│
├── core/
│   ├── path_utils.py
│   ├── usb_watcher.py
│   ├── device_parser.py
│   ├── policy_engine.py
│   ├── usb_blocker.py
│   ├── auditor.py
│   └── logger.py
│
├── gui/
│   └── dashboard.py
│
├── logs/
│   └── usb_activity.log
│
└── data/
    └── usb_events.json
