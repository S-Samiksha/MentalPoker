
import socket
import gmpy2
from Crypto.Util.number import *
from Crypto import Random
import Crypto
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

p = 223621388031669181155297260782194064943
q = 245132897482391278543047151822806952741
n = p*q
PHI=(p-1)*(q-1) #phi value 
e_key = 65537 #default
d_key = gmpy2.invert(e_key, PHI) #default

class key:
    def __init__(self):
        e_key = Crypto.Util.number.getPrime(12, randfunc=Crypto.Random.get_random_bytes)
        d_key = gmpy2.invert(e_key, PHI)
        print("Your Encryption Key is: ", e_key)
        print("Your Decryption Key is: ", d_key)

    def card_encrypt(slef, msg):
        m = bytes_to_long(msg.encode())
        c1 = pow(m, e_key, n)
        valsend = str(c1)
        return valsend

    def card_decrypt(self, c2):
        val = int(c2)
        d1 = pow(val,d_key,n)
        byt_val = long_to_bytes(d1)
        msg = byt_val.decode()
        return msg

    def bob_alice_encrypt(self, msg):
        return str(pow(int(msg), e_key, n))
    
    def alice_decrypt_bob(self, msg):
        return str(pow(int(msg), d_key, n))
