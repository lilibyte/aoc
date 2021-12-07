f = sorted(int(i) for i in open("input").read().strip().split(","))

l, p2 = 0, [0 for x in range(f[-1] + 1)]

for i in range(f[-1] + 1):
    for cr in f:
        # thank you No.84646327-senpai
        p2[i] += (abs(cr - i) + 1) * abs(cr - i) // 2
        # p2[i] += sum(range(1, abs(cr - i) + 1))
    if l and l < p2[i]:
        break
    l = p2[i]

print(sum(abs(f[len(f) // 2] - cr) for cr in f))
print(min(i for i in p2 if i > 0))
