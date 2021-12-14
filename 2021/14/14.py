from collections import defaultdict

f = [l.strip() for l in __import__('fileinput').input() if l.strip()]
pt, pi = defaultdict(int), dict([r.split(" -> ") for r in f[1:]])
ch = defaultdict(int)

for i in range(len(f[0]) - 1):
    pt[f[0][i] + f[0][i + 1]] += 1
    ch[f[0][i]] += 1
ch[f[0][i+1]] += 1

for i in range(40):
    aux = pt.copy()
    for k, v in aux.items():
        ch[pi[k]] += aux[k]
        pt[k] -= aux[k]
        pt[k[0] + pi[k]] += aux[k]
        pt[pi[k] + k[1]] += aux[k]
    if i in (9, 39):
        s = sorted(ch, key=lambda x: ch[x])
        print(ch[s[-1]] - ch[s[0]])

# pt = list(f[0])

# for _ in range(10):
#     if not _ % 5:
#         print(_)
#     r = {}
#     for i, x in enumerate(pt):
#         if i < len(pt) - 1 and "".join(pt[i:i+2]) in pi:
#             r[i] = pi[pt[i] + pt[i + 1]]
#     test = 0
#     for i, m in r.items():
#         pt.insert(i + 1 + test, m)
#         test += 1

# mc = lc = 0
# for c in set(pt):
#     if (t := pt.count(c)) > mc:
#         mc = t
#     if t < lc or not lc:
#         lc = t

# print(mc - lc)
