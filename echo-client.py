# Derived from https://realpython.com/python-sockets/#echo-client-and-server

import socket

HOST = "10.27.251.159"  # The server's hostname or IP address
PORT = 53142  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello again")
    data = s.recv(1024)

    print(f"Received {data!r}")

    
    