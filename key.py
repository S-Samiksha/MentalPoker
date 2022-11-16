
import socket
import gmpy2
from Crypto.Util.number import *
from Crypto import Random
import Crypto
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# p = 223621388031669181155297260782194064943 #128 bit
# q = 245132897482391278543047151822806952741 #128 bit 

# p = 12880975502056481219 # 64 bits
# q = 9362325759663768767 # 64 bits

# p = 4192394699 #32 bits
# q = 2921148821 #32 bits

p=233
q=211

n = p*q
PHI=(p-1)*(q-1) #phi value 
# e_key = 65537 #default
# d_key = gmpy2.invert(e_key, PHI) #default


class key:

    def __init__(self):
        while True:
            self.e_key = Crypto.Util.number.getPrime(8, randfunc=Crypto.Random.get_random_bytes)
            self.d_key = gmpy2.invert(self.e_key, PHI)
            if (self.d_key > int((1/3)*(n)**(1/4))):
                break
            else:
                continue

        print("Your Encryption Key is: ", self.e_key)
        print("Your Decryption Key is: ", self.d_key)

    def card_encrypt(self, msg):
        m = bytes_to_long(msg.encode())
        c1 = pow(m, self.e_key, n)
        valsend = str(c1)
        return valsend

    def card_decrypt(self, c2):
        val = int(c2)
        d1 = pow(val,self.d_key,n)
        byt_val = long_to_bytes(d1)
        msg = byt_val.decode()
        return msg

    def bob_alice_encrypt(self, msg):
        return str(pow(int(msg), self.e_key, n))
    
    def alice_decrypt_bob(self, msg):
        return str(pow(int(msg), self.d_key, n))

    def return_keys(self):
        return self.e_key, self.d_key

    def decrypt_other(self,c2, other_key):
        val = int(c2)
       
        d1 = pow(val,int(other_key),n)
        byt_val = long_to_bytes(d1)
        msg = byt_val.decode()
        return msg

    def return_e_n(self):
        return self.e_key, n