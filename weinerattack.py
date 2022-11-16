import socket
import gmpy2
from Crypto.Util.number import *
from Crypto import Random
import Crypto
from sympy import mod_inverse
import math 
from weinerattack2 import *

p = 4192394699 #32 bits
q = 2921148821 #32 bits

n = p*q
PHI=(p-1)*(q-1) #phi value 
#e_key = Crypto.Util.number.getPrime(16, randfunc=Crypto.Random.get_random_bytes)

print("Value of phi(n): ", PHI)
print("Value of n: ", n)
d_key = int((1/3)*(n)**(1/4))
print("Value of smallest d: ", d_key)


count = 0
for i in range(100, d_key):
    try: 
        e = mod_inverse(i, PHI)
        print("Hihi")
        d = weinerAttack(e, n)
        print("Value of e: ", e)
        #print("Value of d: ", d)
        print("Phi is greater than e:", PHI>e)
        count += 1
        break
        if (count > 10):
            break
    except:
        count+=1
        continue
