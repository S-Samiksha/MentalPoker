
import socket
import gmpy2
from Crypto.Util.number import *
from Crypto import Random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

p = 223621388031669181155297260782194064943
q = 245132897482391278543047151822806952741
# p=13
# q=7
n = p*q
PHI=(p-1)*(q-1) #phi value 
e_bob = 65537
d_bob = gmpy2.invert(e_bob, PHI)


def bob_encrypt(msg):
    m = bytes_to_long(msg.encode())
    c1 = pow(m, e_bob, n)
    valsend = str(c1)
    return valsend

def bob_decrypt(c2):
    val = int(c2)
    d1 = pow(val,d_bob,n)
    byt_val = long_to_bytes(d1)
    msg = byt_val.decode()
    return msg

def bob_encrypt_alice(msg):
    return str(pow(int(msg), e_bob, n))