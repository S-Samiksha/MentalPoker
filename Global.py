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
BITS = 128


PARAMETER = dh.generate_parameters(generator=2, key_size=512)
results = PARAMETER.parameter_numbers()

p = Crypto.Util.number.getPrime(BITS, randfunc=Crypto.Random.get_random_bytes) #get a random p prime 
q = Crypto.Util.number.getPrime(BITS, randfunc=Crypto.Random.get_random_bytes) #get a random q prime 
n = p*q #n value this has to be shared between alice and bob 


def return_paramter():
    print(results.p, results.g)
    return PARAMETER

def return_rsa():
    return p,q,n
