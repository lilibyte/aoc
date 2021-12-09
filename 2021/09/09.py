from functools import reduce
from operator import mul

f = [[int(i) for i in l.strip()] for l in __import__('fileinput').input()]

p1 = p2 = 0
t, lp = [], []


for y, l in enumerate(f):
    for x, i in enumerate(l):
        if (not y or f[y - 1][x] > i) and (y == len(f) - 1 or f[y + 1][x] > i):
            if (not x or f[y][x - 1] > i) and (x == len(l) - 1 or f[y][x + 1] > i):
                p1 += (i + 1)
                lp.append((y, x))

print(p1)

def check_pos(y, x):
    aux = []
    if y and f[y - 1][x] != 9:
        aux.append((y - 1, x))
    if y < len(f) - 1 and f[y + 1][x] != 9:
        aux.append((y + 1, x))
    if x and f[y][x - 1] != 9:
        aux.append((y, x - 1))
    if x < len(f[y]) - 1 and f[y][x + 1] != 9:
        aux.append((y, x + 1))
    return aux

for c in lp:
    y, x = c
    b = set()
    b.add((y, x))
    aux = check_pos(y, x)
    for c in aux:
        b.add(c)
    prev = 0
    while True:
        aux = []
        for c in b:
            aux.extend(check_pos(c[0], c[1]))
        for c in aux:
            b.add(c)
        if len(b) == prev:
            break
        prev = len(b)
    t.append(len(b))

print(reduce(mul, sorted(t)[-3:], 1))
