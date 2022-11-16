# Adapted from https://cryptography.io/en/latest/hazmat/primitives/asymmetric/dh/ 

from Crypto.Util.number import *
from Crypto import Random
import Crypto
import gmpy2
import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
BITS = 16


p = Crypto.Util.number.getPrime(BITS, randfunc=Crypto.Random.get_random_bytes) #get a random p prime 
q = Crypto.Util.number.getPrime(BITS, randfunc=Crypto.Random.get_random_bytes) #get a random q prime 
n = p*q #n value this has to be shared between alice and bob 
print(p)
print(q)


