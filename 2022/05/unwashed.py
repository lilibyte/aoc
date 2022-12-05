from aoc import input
from collections import deque

CRATES = 9
RANGE = 34
I = input().split("\n")
C = I[:CRATES-1]
crates = [deque() for _ in range(CRATES)]
crates2 = [deque() for _ in range(CRATES)]
ins = I[CRATES+1:len(I)-1]
for line in C:
	for c, i in enumerate(range(1, RANGE + 3, 4)):
		if line[i] != " ":
			crates[c].append(line[i])
			crates2[c].append(line[i])

for op in ins:
	op = op.split()
	n = int(op[1])
	fr = int(op[3])
	to = int(op[5])
	tmp = []
	for _ in range(n):
		crates[to-1].appendleft(crates[fr-1].popleft())
		tmp.append(crates2[fr-1].popleft())
	for c in reversed(tmp):
		crates2[to-1].appendleft(c)

print("".join(crate[0] for crate in crates if crate))
print("".join(crate[0] for crate in crates2 if crate))
