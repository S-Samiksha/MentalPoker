# Derived from https://realpython.com/python-sockets/#echo-client-and-server
# Derived from https://medium.com/asecuritysite-when-bob-met-alice/bob-and-alice-play-mental-poker-in-a-world-where-they-trust-no-one-6cc557596169 

#Application usage for Alice

import socket
import gmpy2
from Crypto.Util.number import *
from Crypto import Random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from Alice_func import *

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~ Alice ready to play ~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 53140  # The port used by the server

while KeyboardInterrupt():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        val = input("Enter your value: ")
        if (len(val)>1):
            msg = val


        # Sending cards --------------
        valsend = alice_encrypt(msg)
        print("Alice Encrypted Value: ", valsend)
        s.connect((HOST, PORT))
        s.sendall(valsend.encode())

        data = s.recv(1024)
        data_bob = data.decode()
        print("Received from Bob: ", data_bob)
        print("Encrypted Bob Message using Alice Key: ", alice_encrypt_bob(data_bob))

        
        #print("Encrypted Bob message with Alice Key: ", long_to_bytes(alice_encrypt(data_bob)))
        







    
    