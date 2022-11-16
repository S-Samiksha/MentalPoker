#Adapted from: https://programmerall.com/article/33411378209/

import gmpy2
def transform(x,y):       
    results=[]
    while y:
        results.append(x//y) 
        x,y=y,x%y #assign the new remainder and the quotient 
    return results
    
def continued_fraction(sub_res):
    numerator,denominator=1,0
    for i in sub_res[::-1]:      #Circulation from the back of Sublist
        denominator,numerator=numerator,i*numerator+denominator  #Continued fraction formula 
    return denominator,numerator   #Get progressive and molecules of progressive fractions, and return

    
#Solve each gradual score
def sub_fraction(x,y):
    res=transform(x,y)
    res=list(map(continued_fraction,(res[0:i] for i in range(1,len(res)))))  #Intercepted the result of the even fraction taken one by one to seek score
    return res

def get_pq(a,b,c):      #The values ​​of P + Q and PQ are solved by Villa's theorem to solve P and Q
    if (b*b-4*a*c<0):
        return -1,-1
    par=gmpy2.isqrt(b*b-4*a*c)   #From the above, the opening role must be an integer because
    x1,x2=(-b+par)//(2*a),(-b-par)//(2*a)
    return x1,x2

def wienerAttack(e,n):
    for (d,k) in sub_fraction(e,n):  #Use a for loop to pay attention to the progressive score of the continuous function of E / N until you find a gradual score that meets the conditions.
        if k==0:                     #There may be a case where the connection is 0 is 0, exclude
            continue
        if (e*d-1)%k!=0:             #ED = 1 (MOD φ (N)) Therefore, if D is found, (ED-1) will except φ (N), that is, k makes (E * D-1) // k = φ (n)
            continue
        
        phi=(e*d-1)//k               #This result is φ (n)
        px,qy=get_pq(1,n-phi+1,n)
        if (px==-1 and qy==-1):
            print("This method is not applicable")
            return
        if px*qy==n:
            p,q=abs(int(px)),abs(int(qy))     #May get two negative numbers, negative negative, no, no
            d=gmpy2.invert(e,(p-1)*(q-1))     #As a result of ED = 1 (MOD φ (N)), that is, E: multiplication reverse element D of φ (n)
            return d
    print("This method is not applicable")
    return
    
    

p = 4192394699 #32 bits
q = 2921148821 #32 bits

n = p*q

e = 8164405883357970907
d=wienerAttack(e,n)
print("d=",d)

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
