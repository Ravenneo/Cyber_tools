import socket
from concurrent.futures import ThreadPoolExecutor
import time
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("ip", type=str, help="Target IP address to scan")
    parser.add_argument("--timeout", type=float, default=1, help="Timeout for port connection")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads for parallel scanning")

    args = parser.parse_args()

    target_ip = args.ip
    timeout_value = args.timeout
    num_threads_value = args.threads

    port_scanner(target_ip, timeout=timeout_value, num_threads=num_threads_value)
