# 2022-12-06

from aoc import input
from collections import Counter

I = input().strip()

cols = [[] for _ in range(8)]

for row in I.split():
	for i, col in enumerate(row):
		cols[i].append(col)

print("".join(Counter(i).most_common()[0][0] for i in cols))
print("".join(Counter(i).most_common()[-1][0] for i in cols))
