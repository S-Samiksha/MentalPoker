# Derived from https://realpython.com/python-sockets/#echo-client-and-server

import socket
import gmpy2
from Crypto.Util.number import *
from Crypto import Random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from Bob_func import *

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~ Bob ready to play ~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 53140  # Port to listen on (non-privileged ports are > 1023)
while (True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                data = conn.recv(1024)
                if not data:
                    break
                


                #Send/Receiving cards ----------------
                data_alice = data.decode()
                print("Recived from Alice: ", data_alice)
                print("Encrypted Alice message with Bob key: ", bob_encrypt_alice(data_alice))
                if not data_alice:
                    break

                
                val = input("Enter your value: ")
                if (len(val)>1):
                    msg = val
                
                valsend = bob_encrypt(msg)
                print("Bob Encrypted Value: ", valsend)
                conn.sendall(valsend.encode())



