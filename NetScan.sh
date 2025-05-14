#!/bin/bash

echo "Starting Bluetooth scan..."

# Start bluetoothctl and scan
bluetoothctl --timeout 15 << EOF | grep -Eo '([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}' | sort | uniq
power on
scan on
EOF

echo "Scan complete."

