import subprocess
import os


def get_devices() -> list:
    devices = []

    for device in os.listdir("/sys/block"):
        if device.startswith("loop") or device.startswith("ram"):
            continue
        devices.append(f"/dev/{device}")
    return devices


def get_smart_status():
    print("wip")
    return


if __name__ == '__main__':
    drive_list = get_devices()
    for drive in drive_list:
        print(drive)
    