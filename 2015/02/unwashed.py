from functools import reduce
from operator import mul
from aoc import scan, static

def surf(l):
	L = 2 * l[0] * l[1]
	W = 2 * l[1] * l[2]
	H = 2 * l[2] * l[0]
	return L, W, H

def sqft(l):
	return sum(l) + min(l) // 2

def rot(l):
	L, W, H = l
	if H < W >= L:
		W, H = H, W
	elif H < L > W:
		L, H = H, L
	return L, W, H

def wrap(l):
	L, W, H = rot(l)
	return L * 2 + W * 2

def bow(l):
	return reduce(mul, l)

@static(t=0)
def p1(l):
	p1.t += sqft(surf(l))
	return p1.t

@static(t=0)
def p2(l):
	p2.t += wrap(l) + bow(l)
	return p2.t

for l in scan(r"(\d+)x(\d+)x(\d+)"):
	p1(l)
	p2(l)

print(p1.t)
print(p2.t)
