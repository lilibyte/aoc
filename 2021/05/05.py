from collections import defaultdict

f = [[(*(map(int, i.split(','))),) for i in l.split() if ',' in i] for l in __import__('fileinput').input(files=('input'))]
p1, p2 = defaultdict(int), defaultdict(int)

for l in f:
    x1, y1, x2, y2 = *l[0], *l[1]
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            p1[(x2, i)] += 1
            p2[(x2, i)] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            p1[(i, y1)] += 1
            p2[(i, y1)] += 1
    else:
        for i in range(max(abs(y1 - y2), abs(x1 - x2)) + 1):
            x, y = x1 - i if x1 > x2 else x1 + i, y1 - i if y1 > y2 else y1 + i
            p2[(x, y)] += 1

print(sum(1 for i in p1.values() if i > 1))
print(sum(1 for i in p2.values() if i > 1))
