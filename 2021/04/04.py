from collections import defaultdict

f = open('input').read().strip().split("\n\n")
dd = defaultdict(list)
w = defaultdict(list)
p = [int(i) for i in f[0].split(",")]
p1, p2 = [0, 0, 0], [[], 0, 0]

for i, b in enumerate(f[1:]):
    for r in b.splitlines():
        dd[i].append([int(x) for x in r.split()])

for i, ins in enumerate(p):
    for bi, b in enumerate(dd.values()):
        for ri, r in enumerate(b):
            if ins in r:
                w[bi].append((ri, r.index(ins)))
                h = [x[0] for x in w[bi]]
                v = [x[1] for x in w[bi]]
                for y in range(5):
                    if h.count(y) == 5 or v.count(y) == 5:
                        if not p1[1]:
                            p1[0], p1[1], p1[2] = bi, i + 1, ins
                        if bi not in p2[0]:
                            p2[0].append(bi)
                            p2[1], p2[2] = i + 1, ins

print(sum(i for r in dd[p1[0]] for i in r if i not in p[:p1[1]]) * p1[2])
print(sum(i for r in dd[p2[0][-1]] for i in r if i not in p[:p2[1]]) * p2[2])
