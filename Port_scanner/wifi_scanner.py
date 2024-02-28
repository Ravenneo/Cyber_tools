# Python

import subprocess

def scan_wifi():
    """Scans for available Wi-Fi networks and returns a list of SSIDs."""
    results = subprocess.run(
        ["iw", "wlan0", "scan"], capture_output=True, text=True
    ).stdout
    networks = []
    for line in results.splitlines():
        if line.startswith("BSS"):
            ssid_start = line.find("SSID:") + 6
            ssid_end = line.find("Signal")
            ssid = line[ssid_start:ssid_end].strip()
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
