# Godot Time Tracker

A simple background service that automatically tracks time spent in Godot Engine.

## Setup

### 1. Install dependencies
```bash
sudo apt install python3-psutil
```
### 2. Create both scripts on your machine 

### 3. Create systemd service
```bash
mkdir -p ~/.config/systemd/user
cat > ~/.config/systemd/user/godot-tracker.service << 'EOF'
[Unit]
Description=Godot Time Tracker
After=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /path/to/time-tracker.py # REPLACE THIS!
Restart=always
RestartSec=5
Environment=HOME=%h

[Install]
WantedBy=default.target
EOF
```

### 4. Enable and Start Service
```bash
chmod +x ~/Games/time-tracker.py
systemctl --user daemon-reload
systemctl --user enable godot-tracker.service
systemctl --user start godot-tracker.service
```

### 5. Create Alias for Easy Access
```bash
echo 'alias godot-time="python3 /path/to/godot-time.py"' >> ~/.bash_aliases # or .bashrc if you don't have an aliases file. Also, remember to change the path
source ~/.bash_aliases
```

## Usage

- **Check time**: `godot-time`
- **Reset time**: `rm ~/.godot_time.json`
- **Check service status**: `systemctl --user status godot-tracker.service`
- **Stop service**: `systemctl --user stop godot-tracker.service`
- **Start service**: `systemctl --user start godot-tracker.service`

## How It Works

- The service runs automatically in the background
- It detects when Godot is running and starts counting time
- Time is saved every minute to `~/.godot_time.json`
