from collections import defaultdict

f = __import__('fileinput').input(files=('input'))
p1, p2 = defaultdict(int), defaultdict(int)

for l in f:
    l = [[int(x) for x in i.split(",")] for i in l.split("->")]
    x1, y1, x2, y2 = *l[0], *l[1]
    xs = -1 if x2 - x1 < 0 else 1 if x2 - x1 > 0 else 0
    ys = -1 if y2 - y1 < 0 else 1 if y2 - y1 > 0 else 0
    for i in range(max(abs(x2 - x1), abs(y2 - y1)) + 1):
        x, y = x1 + xs * i, y1 + ys * i
        p2[x, y] += 1
        if min(abs(x2 - x1), abs(y2 - y1)) == 0:
            p1[x, y] += 1

print(sum(1 for i in p1.values() if i > 1))
print(sum(1 for i in p2.values() if i > 1))
