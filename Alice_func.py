

import socket
import gmpy2
from Crypto.Util.number import *
from Crypto import Random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

p = 223621388031669181155297260782194064943
q = 245132897482391278543047151822806952741
# p= 311664906201160519894934327413000562173
# q = 241527376067354750589215618199240182167
# p= 13
# q=29
n = p*q
PHI=(p-1)*(q-1) #phi value this is shared between alice and bob
e_alice = 65539 
d_alice = gmpy2.invert(e_alice, PHI)
print(d_alice)

def alice_encrypt(msg):
    m = bytes_to_long(msg.encode())
    c1=pow(m,e_alice, n)  #M^(e_alice) mod n it is to be noted that this is in integer format 
    valsend = str(c1)
    return valsend

def alice_decrypt(c2):
    val = int(c2)
    d1=pow(val,d_alice, n)
    print(d1)
    byt_val = long_to_bytes(d1)
    print(byt_val)
    msg = byt_val.decode()
    print(msg)
    return msg

def alice_encrypt_bob(msg):
    return pow(int(msg),e_alice, n)

def alice_decrypt_bob(msg):
    return str(pow(int(msg), d_alice, n))




    