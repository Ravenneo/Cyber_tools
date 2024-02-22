import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("Open port: " + str(port))
    except socket.error:
        print("Error connecting to port: " + str(port))
    finally:
        sock.close()

def port_scanner(ip, timeout=1, num_threads=10):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(scan_port, ip, port, timeout) for port in range(1, 65535)]

        # Wait for all threads to complete
        for future in futures:
            future.result()

if __name__ == "__main__":
    target_ip = input("write IP: ")
    port_scanner(target_ip)
