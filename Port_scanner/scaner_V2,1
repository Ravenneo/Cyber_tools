import socket
from concurrent.futures import ThreadPoolExecutor
import time

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

if __name__ == "__main__":
    target_ip = input("Enter IP address to scan: ")
    port_scanner(target_ip)
