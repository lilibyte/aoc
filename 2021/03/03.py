f = [l.strip() for l in __import__('fileinput').input(files=('input'))]
d = {i: [0, 0] for i in range(12)}

def pd(f=f, d=d):
    for n in f:
        for i, b in enumerate(n):
            d[i][int(b)] += 1

pd()

gr = int("".join([str(int(i[1] > i[0])) for i in d.values()]), 2)
ep = int("".join([str(int(i[1] < i[0])) for i in d.values()]), 2)

print(ep * gr)

d2 = d
f2 = f.copy()
e2 = e = 0

for i in range(12):
    if len(f) > 2:
        f = [l for l in f if l[i] == str(int(d[i][1] >= d[i][0]))]
        d = {i: [0, 0] for i in range(12)}
        pd(f, d)
        e += 1
    if len(f2) > 2:
        f2 = [l for l in f2 if l[i] == str(int(d2[i][1] < d2[i][0]))]
        d2 = {i: [0, 0] for i in range(12)}
        pd(f2, d2)
        e2 += 1

o = int(f[0] if f[0][e] == 1 else f[1], 2) if len(f) > 1 else int(f[0], 2)
c = int(f2[0] if f2[0][e2] == 0 else f2[1], 2) if len(f2) > 1 else int(f2[0], 2)

print(o * c)
