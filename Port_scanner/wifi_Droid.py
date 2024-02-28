# Python

import subprocess

def scan_wifi():
    """Scans for available Wi-Fi networks and returns a list of SSIDs."""
    results = subprocess.run(
        ["iw", "wlan0", "scan"], capture_output=True, text=True
    ).stdout
    networks = []
    in_block = False
    for line in results.splitlines():
        if line.startswith("BSS"):
            in_block = True
        elif line.strip() == "":
            in_block = False
        elif in_block and line.strip().startswith("SSID"):
            ssid = line.split(":", 1)[1].strip()
            networks.append(ssid)
    return networks

if __name__ == "__main__":
    available_networks = scan_wifi()
    if available_networks:
        print("Available Wi-Fi networks:")
        for network in available_networks:
            print(f" - {network}")
    else:
        print("No Wi-Fi networks found.")