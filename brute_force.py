import socket
import gmpy2
from Crypto.Util.number import *
from Crypto import Random
import Crypto
from sympy import mod_inverse

# I know p and q
p = 4192394699 #32 bits
q = 2921148821 #32 bits
n = p*q
PHI=(p-1)*(q-1) #phi value 

# Encryption key has to satisfy the property gcd(e, phi(n)) = 1 in other words, there exists an inverse 

possible_e = []

for i in range (PHI):
    try:
        mod_inverse(i, PHI)
        possible_e.append(i)
    except:
        continue

print(possible_e)


