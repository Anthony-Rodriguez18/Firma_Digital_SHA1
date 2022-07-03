import hashlib 
import random  

def EXPMOD(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y>>1
        x = (x * x) % p

    return res

def COMPUESTO(d, n):
    a = 2 + random.randint(1, n - 4)
    x = EXPMOD(a, d, n)
  
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n 
        d *= 2

        if (x == 1):
            return False
        if (x == n - 1):
            return True
    # Return compuesto
    return False

def Miller( n, s):
    if (n <= 1 or n == 4):
      return False
    if (n <= 3):
      return True
    u = n - 1
    while (u % 2 == 0):
      u//= 2
    for i in range(s):
      if (COMPUESTO(u, n) == False):
        return False

    return True
  
def EUCLIDES(a,b):
    if b == 0:
        return a
    else:
        return EUCLIDES(b, a%b)

def EUCLIDESEXT(a,b):
    if b == 0:
        return(a,1,0)
    else:
        (d,x1,y1) = EUCLIDESEXT(b, a%b)
        aux = a/b
        p= int(aux)
        (x,y) = (y1, x1-(p*y1))
        return(d,x,y)

def inverso(a,n):
       
    if EUCLIDES(a,n) == 1:
        (p,x,y)=EUCLIDESEXT(a,n)
        m =x%n
        return m
 

def PRIMO(n,s):
  for _ in iter(int, 1):
    b = random.getrandbits(n)
    if (Miller(b, s)):
      return(b)

def RSA(k):
  bit=k/2
  com = True
  while (com):
    p = PRIMO(int(bit),43)
    q = PRIMO(int(bit),43)
    if(p!=q):
      com=False
  n = (p*q)
  fin = ((p-1)*(q-1))
  seg = True
  while (seg):
    e=random.randint(2,(n-1))
    if(EUCLIDES(e,fin)==1):
      seg=False
  d=inverso(e,fin)
  return (n,e,d)
  
def cifrado(M,N,E):
  a=EXPMOD(M, E, N)
  return a

def decifrado(C,N,D):
  m=EXPMOD(C, D, N)
  return m



(n,e,d)=RSA(32)
h=hashlib.sha1()

mensajes=["Hola Mundo","CASA SOLA","MARVEL:END GAME"]
M=[]
HASH=[]
FIR=[]
DEC=[]
DIC=[]

for mensaje in mensajes:
  h.update(bytes(mensaje,encoding='utf-8'))
  hash_mensaje=h.hexdigest()
  HASH.append(hash_mensaje)
  m=random.randint(1,(n-1))
  M.append(m)
  dic={hash_mensaje,m}
  DIC.append(dic)
  fir=decifrado(m,n,e)
  FIR.append(fir)

for men in FIR:
  dm=cifrado(men,n,d)
  DEC.append(dm)

print("MENSAJES =",mensajes)
print("HASH =",HASH)
print("M =",M)
print("FIRMA =",FIR)
print("P(A) =",DEC)





