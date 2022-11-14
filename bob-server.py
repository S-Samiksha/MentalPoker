# Derived from https://realpython.com/python-sockets/#echo-client-and-server

import socket
import gmpy2
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from Global import return_rsa


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 53141  # Port to listen on (non-privileged ports are > 1023)

p = 223621388031669181155297260782194064943
q = 245132897482391278543047151822806952741
n = p*q
PHI=(p-1)*(q-1) #phi value 
e_bob = 65537
d_bob = gmpy2.invert(e_bob, PHI)

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
