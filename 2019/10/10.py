from math import atan2

f = [list(l.strip()) for l in __import__('fileinput').input()]
crds = [(y, x) for y, r in enumerate(f) for x, c in enumerate(r) if c == "#"]

totals = []
for i1, c1 in enumerate(crds):
    atan2_results = set()
    for i2, c2 in enumerate(crds):
        if not i2 == i1:
            atan2_results.add(atan2(c1[0] - c2[0], c1[1] - c2[1]))
    totals.append(len(atan2_results))

print(max(totals))
