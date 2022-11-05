# Derived from https://realpython.com/python-sockets/#echo-client-and-server
# Derived from https://medium.com/asecuritysite-when-bob-met-alice/bob-and-alice-play-mental-poker-in-a-world-where-they-trust-no-one-6cc557596169 

#Application usage for Alice

import socket
from Crypto.Util.number import *
from Crypto import Random
import Crypto
import gmpy2
import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

q

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 53142  # The port used by the server




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    val = input("Enter your value: ")
    if (len(val)>1):
        msg = val
    


    s.connect((HOST, PORT))
    s.sendall(msg.encode())
    data = s.recv(1024)

    print(f"Received {data!r}")







'''
RSA Codes:

p = Crypto.Util.number.getPrime(BITS, randfunc=Crypto.Random.get_random_bytes) #get a random p prime 
q = Crypto.Util.number.getPrime(BITS, randfunc=Crypto.Random.get_random_bytes) #get a random q prime 
n = p*q #n value this has to be shared between alice and bob 
PHI=(p-1)*(q-1) #phi value 

# RSA Encrytion keys
e_bob=65537 #seems like this is the private
e_alice=65539 #seems like this is the private
d_alice=(gmpy2.invert(e_bob, PHI))

m = bytes_to_long(msg.encode('utf-8'))
c1=pow(m,e_alice, n) #M^(e_alice) mod n it is to be noted that this is in integer format 
print("Sending Encrypted Value: ", c1)
valsend = str(c1)

'''
    
    