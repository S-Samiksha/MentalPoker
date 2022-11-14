# Derived from https://realpython.com/python-sockets/#echo-client-and-server

import socket
import gmpy2
from Crypto.Util.number import *
from Crypto import Random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~ Bob ready to play ~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
p = 223621388031669181155297260782194064943
q = 245132897482391278543047151822806952741
n = p*q
PHI=(p-1)*(q-1) #phi value 
e_bob = 65537
d_bob = gmpy2.invert(e_bob, PHI)

def bob_encrypt(msg):
    m = bytes_to_long(msg.encode('utf-8'))
    c1 = pow(m, e_bob, n)
    valsend = str(c1)
    return valsend

def bob_decrypt(c2):
    val = int(c2)
    d1 = pow(val,d_bob,n)
    byt_val = long_to_bytes(d1)
    msg = byt_val.decode('utf-8')
    return msg


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 53140  # Port to listen on (non-privileged ports are > 1023)
while (KeyboardInterrupt()):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while KeyboardInterrupt():
                data = conn.recv(1024)
                data_alice = data.decode()
                print("Recived from Alice: ", data_alice)
                if not data_alice:
                    break

                
                val = input("Enter your value: ")
                if (len(val)>1):
                    msg = val
                
                valsend = bob_encrypt(msg)
                conn.sendall(valsend.encode())

