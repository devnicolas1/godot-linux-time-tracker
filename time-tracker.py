#!/usr/bin/env python3
import psutil
import time
import json
import os

data_file = os.path.expanduser("~/.godot_time.json")

try:
    with open(data_file, 'r') as f:
        total_time = json.load(f).get('total', 0)
except:
    total_time = 0

while True:
    godot_running = any('godot' in p.name().lower() for p in psutil.process_iter(['name']) if p.name())
    if godot_running:
        total_time += 1
        if total_time % 60 == 0:
            with open(data_file, 'w') as f:
                json.dump({'total': total_time}, f)

    time.sleep(1)
