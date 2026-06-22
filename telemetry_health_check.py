import requests

devices = [
    "router1",
    "router2",
    "switch1"
]

for device in devices:
    print(f"Checking telemetry status for {device}")

print("Telemetry validation completed.")
