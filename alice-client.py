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

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~ Alice ready to play ~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
p = 223621388031669181155297260782194064943
q = 245132897482391278543047151822806952741
n = p*q
PHI=(p-1)*(q-1) #phi value this is shared between alice and bob
e_alice = 65539 
d_alice = gmpy2.invert(e_alice, PHI)

def alice_encrypt(msg):
    m = bytes_to_long(msg.encode('utf-8'))
    c1=pow(m,e_alice, n)  #M^(e_alice) mod n it is to be noted that this is in integer format 
    valsend = str(c1)
    return valsend

def alice_decrypt(c2):
    val = int(c2)
    d1=pow(val,d_alice, n)
    byt_val = long_to_bytes(d1)
    msg = byt_val.decode('utf-8')
    return msg


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 53140  # The port used by the server

while KeyboardInterrupt():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        val = input("Enter your value: ")
        if (len(val)>1):
            msg = val
        
        valsend = alice_encrypt(msg)
        print("Alice Encrypted Value: ", valsend)
        s.connect((HOST, PORT))
        s.sendall(valsend.encode())

        data = s.recv(1024)
        data_bob = data.decode()
        print("Received from Bob: ", data_bob)
        print("Encrypted Bob Message using Alice Key: ", pow(int(data_bob),e_alice, n))

        
        #print("Encrypted Bob message with Alice Key: ", long_to_bytes(alice_encrypt(data_bob)))
        







    
    