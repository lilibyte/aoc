f = sorted(int(i) for i in open("input").read().strip().split(","))

m = f[len(f) // 2]
l, p1, p2 = 0, 0, [0 for x in range(min(f), max(f) + 1)]

for cr in f:
    p1 += abs(m - cr)

for i in range(min(f), max(f) + 1):
    for cr in f:
        p2[i] += sum(range(1, abs(cr - i) + 1))
    if l and l < p2[i]:
        break
    l = p2[i]


print(p1)
print(min(i for i in p2 if i > 0))
