import math
import os
import numpy

def keys(key,shift):
	for i in range(0,(shift*25)):
		key = [key[1:length(key)],key[0]]
	k1 = key[0]+key[1]
	k2 = key[2]+key[3]
	k3 = key[4]+key[5]
	k4 = key[6]+key[7]
	k5 = key[8]+key[19]
	k6 = key[10]+key[11]
	k7 = key[12]+key[13]
	k8 = key[14]+key[15]
	return[k1,k2,k3,k4,k5,k6,k7,k8]


key = "ABCDEFGHIJKLMNOP"
keyA = [ord(c) for c in key]
print(keyA)

plainText = "Hello! This is my secret message"
pb = [ord(c) for c in plainText]
print(pb)
l = len(pb)
p1 = pb[0:math.floor(l/4)]
p2 = pb[math.floor(l/4):math.floor(l/2)]
p3 = pb[math.floor(l/2):math.floor(l/2)+math.floor(l/4)]
p4 = pb[math.floor(l/2)+math.floor(l/4):l]
print(p1+p2+p3+p4)
print(keys(keyA,0))
