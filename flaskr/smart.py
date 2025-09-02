import subprocess
import os


def get_devices() -> list:
    devices = []

    for device in os.listdir("/sys/block"):
        if device.startswith("loop") or device.startswith("ram"):
            continue
        devices.append(f"/dev/{device}")
    return devices
