import socket

ip = input("write IP: ")
Timeout = 1
for port in range(1,65535):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(Timeout)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print("Open port: " + str(port))
    else:
        print("Port close: " + str(port))
sock.close()
