f = [l.strip() for l in __import__('fileinput').input()]

op = {"(": ")", "[": "]", "{": "}", "<": ">"}
scp = {")": 3, "]": 57, "}": 1197, ">": 25137}
acp = {")": 1, "]": 2, "}": 3, ">": 4}
cl = {c: o for o, c in op.items()}
p1, p2, il, s = 0, 0, [], []

for l in f:
    cc = []
    for i, c in enumerate(l):
        if c in op:
            cc.append(c)
        else:
            if not cl[c] == cc[-1]:
                p1 += scp[c]
                break
            else:
                cc.reverse()
                cc.remove(cl[c])
                cc.reverse()
    else:
        t = 0
        cc = []
        for c in reversed(l):
            if c in cl:
                cc.append(c)
            elif op[c] in cc:
                cc.reverse()
                cc.remove(op[c])
                cc.reverse()
            else:
                t *= 5
                t += acp[op[c]]
        s.append(t)
        continue

print(p1)
print(sorted(s)[len(s)//2])
