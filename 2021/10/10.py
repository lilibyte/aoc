f = [l.strip() for l in __import__('fileinput').input()]

op = {"(": ")", "[": "]", "{": "}", "<": ">"}
scp = {")": 3, "]": 57, "}": 1197, ">": 25137}
acp = {")": 1, "]": 2, "}": 3, ">": 4}
cl = {c: o for o, c in op.items()}
p1, p2 = 0, []

for l in f:
    cc = []
    for c in l:
        if c in op:
            cc.append(c)
        else:
            if not cl[c] == cc[-1]:
                p1 += scp[c]
                break
            else:
                del cc[-1]
    else:
        t, cc = 0, []
        for c in reversed(l):
            if c in cl:
                cc.append(c)
            elif op[c] in cc:
                del cc[-1]
            else:
                t *= 5
                t += acp[op[c]]
        p2.append(t)

print(p1)
print(sorted(p2)[len(p2) // 2])
