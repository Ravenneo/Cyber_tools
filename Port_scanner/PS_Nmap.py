import socket
from concurrent.futures import ThreadPoolExecutor
import time
import nmap
import sys
import argparse

def scan_port(ip, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Open port: {port}")
    except socket.error:
        print(f"Error connecting to port: {port}")
    finally:
        sock.close()

def port_scanner(ip, timeout=1, num_threads=10):
    print(f"Scanning ports for {ip}...")
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(scan_port, ip, port, timeout) for port in range(1, 65535)]

        # Wait for all threads to complete
        for future in futures:
            future.result()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Scan completed in {total_time:.2f} seconds.")

    # Additional Nmap Scan
    nm_scan = nmap.PortScanner()
    print('\nRunning Nmap Scan...\n')
    nm_scanner = nm_scan.scan(ip, '80', arguments='-O')

    host_is_up = "The host is: " + nm_scanner['scan'][ip]['status']['state'] + ".\n"
    port_open = "The port 80 is " + nm_scanner['scan'][ip]['tcp'][80]['state'] + ".\n"
    method_scan = "The method of scan is: " + nm_scanner['scan'][ip]['tcp'][80]['state'] + ".\n"

    if 'osmatch' in nm_scanner['scan'][ip]:
        guessed_os = "There is a %s percent chance that the host is running %s" % (nm_scanner['scan'][ip]['osmatch'][0]['accuracy'], nm_scanner['scan'][ip]['osmatch'][0]['name']) + ".\n"
    else:
        guessed_os = "The host's operating system could not be determined.\n"

    with open(f"{ip}_report.txt", 'w') as f:
        f.write(host_is_up + port_open + method_scan + guessed_os)
        f.write("\nReport generated " + time.strftime("%y-%m-%d_%H:%M:%S GMT", time.gmtime()))

    print("\nNmap Scan Finished...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner with Nmap")
    parser.add_argument("ip", type=str, help="Target IP address to scan")
    parser.add_argument("--timeout", type=float, default=1, help="Timeout for port connection")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads for parallel scanning")

    args = parser.parse_args()

    target_ip = args.ip
    timeout_value = args.timeout
    num_threads_value = args.threads

    port_scanner(target_ip, timeout=timeout_value, num_threads=num_threads_value)
