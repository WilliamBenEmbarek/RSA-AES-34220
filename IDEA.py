import math
import os
import numpy
maxval = 2**16
def keyd(kenya):
	shift = 0
	out=[None]*8
	kenya = bin(kenya)[2:]
	t = kenya
	for i in range(8):
		for j in range(0,i*25):
			t  = t[1:128]+t[0]
		out[i] = t
		shift = shift+1
		t = kenya
	out = ''.join(out)
	out = [out[i:i+16] for i in range(0,len(out),16)]
	out = [int(a,2) for a in out]
	return out

def add(x,y):
	return (x+y)%(2**16)

def mul(x,y):
	if x == 0:
		x = 2**16
	if y == 0:
		y = 2**16
	t = (x*y) %(2**(16)+1)
	if t == 2**16:
		t = 0
	return t

def xor(x,y):
	t = x ^ y
	return t

def decSeq(Kanye):
	kd = [None]*52
	kd[0] = invmodp(Kanye[48],2**16+1)
	kd[1] = maxval-Kanye[49]
	kd[2] = maxval-(Kanye[50])
	kd[3] = invmodp(Kanye[51],2**16+1)
	for x in range(8):
		kd[4+6*x] = (Kanye[46-6*x])
		kd[5+6*x] = (Kanye[47-6*x])
		kd[6+6*x] = invmodp(Kanye[42-6*x],2**16+1)
		kd[7+6*x] = maxval-(Kanye[43-6*x])
		kd[8+6*x] = maxval-(Kanye[44-6*x])
		kd[9+6*x] = invmodp(Kanye[45-6*x],2**16+1)
	return kd

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def invmodp(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def encrypt(a,b,c,d,keyA):
	C = 0
	k = keyd(keyA)
	for i in range(8):
		(a,b,c,d,C) = IDEA(a, b, c, d, C,k)

	a1 = mul(a,k[C])
	C = C+1
	b1 = add(c,k[C])
	C = C+1
	c1 = add(b,k[C])
	C = C+1
	d1 = mul(d,k[C])
	C = C+1
	return(a1,b1,c1,d1)

def decrypt(a,b,c,d,keyA):
	C = 0
	kd = decSeq(keyd(keyA))
	for i in range(8):
		(a,b,c,d,C) = IDEA(a, b, c, d, C,kd)
	a1 = mul(a,kd[C])
	C = C+1
	b1 = add(c,kd[C])
	C = C+1
	c1 = add(b,kd[C])
	C = C+1
	d1 = mul(d,kd[C])
	C = C+1
	return(a1,b1,c1,d1)

def IDEA(a,b,c,d,C,k):
	#PREROUND
	t1 = mul(a,k[C])
	C = C+1
	t2 = add(b,k[C])
	C = C+1
	t3 = add(c,k[C])
	C = C+1
	t4 = mul(d,k[C])
	C = C+1
	#SUBROUND1
	t5 = xor(t1,t3)
	t6 = xor(t2,t4)
	#SUBROUND2
	t7 = mul(t5,k[C])
	C = C+1
	t8 = add(t6,t7)
	#SUBROUND3
	t9 = mul(t8,k[C])
	C = C+1
	t10 = add(t9,t7)

	#SUBROUND4
	a = xor(t1,t9)
	b = xor(t3,t9) # Here we swap B and C
	c = xor(t2,t10) # Here we swap B and C
	d = xor(t4,t10)
	return a,b,c,d,C

keyA = 2**128-1
a = 0
b = 0
c = 0
d = 0
print(a,b,c,d)
(a1,b1,c1,d1) = encrypt(a,b,c,d,keyA)
enc = (a1,b1,c1,d1)
print(enc)
dec = decrypt(a1,b1,c1,d1,keyA)
print(dec)