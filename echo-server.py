# Derived from https://realpython.com/python-sockets/#echo-client-and-server

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 53142  # Port to listen on (non-privileged ports are > 1023)

while (True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                print(data.decode())
                if data.decode() == "end":
                    s.close() 
                    exit()

                print(data)
                conn.sendall(b"Hello from server :-)")
