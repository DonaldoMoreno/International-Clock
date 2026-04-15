# International Clock Dashboard (Raspberry Pi 3)

Lightweight fullscreen international clock dashboard built with Python Tkinter, optimized for Raspberry Pi 3 kiosk usage.

## Features

- Fullscreen dark-theme dashboard (ESC exits fullscreen)
- Local time (`HH:MM:SS` or `12h` configurable) and current date
- International clocks for:
  - Mexico City
  - New York
  - London
  - Tokyo
  - Berlin
- 1-second refresh loop with low overhead (`after(1000)`)
- `zoneinfo`-based timezone handling (standard library)
- Configurable cities, colors, fonts, and time format via `config.py`
- Extension hooks for weather, traffic, and second display integrations

## Project Layout

```text
international_clock/
├── main.py
├── ui/
│   └── main_window.py
├── core/
│   └── clock_service.py
├── config.py
└── README.md
```

## Requirements

- Python 3.9+
- Tkinter installed (usually included on Raspberry Pi OS)

## Run

From repository root:

```bash
python -m international_clock.main
```

## Configuration

Edit `international_clock/config.py` to customize:

- `CITIES`
- `COLORS`
- `FONTS`
- `USE_24_HOUR_FORMAT`

## Raspberry Pi Autostart

### Option A: LXDE autostart (kiosk)

1. Create/update autostart file:

```bash
mkdir -p ~/.config/lxsession/LXDE-pi
nano ~/.config/lxsession/LXDE-pi/autostart
```

2. Add:

```text
@xset s off
@xset -dpms
@xset s noblank
@python -m international_clock.main
```

3. Reboot.

### Option B: systemd service

Create `/etc/systemd/system/international-clock.service`:

```ini
[Unit]
Description=International Clock Dashboard
After=graphical.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/International-Clock
Environment=DISPLAY=:0
ExecStart=/usr/bin/python3 -m international_clock.main
Restart=always
RestartSec=5

[Install]
WantedBy=graphical.target
```

Enable service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable international-clock.service
sudo systemctl start international-clock.service
```

## Extension Hooks (placeholders)

`MainWindow` exposes hook setters for future integrations:

- `set_weather_hook(...)`
- `set_traffic_hook(...)`
- `set_second_display_hook(...)`

These are intentionally lightweight extension points and are not fully implemented.
