#!/usr/bin/env python3
import json
import os

try:
    with open(os.path.expanduser('~/.godot_time.json'), 'r') as f:
        total = json.load(f)['total']
    print(f'Total Godot time: {total//3600}h {(total%3600)//60}m')
except:
    print('No time tracked yet')
