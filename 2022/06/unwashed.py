from aoc import input
from more_itertools import sliding_window

I = input().strip()

for i, group in enumerate(sliding_window(I, 4), start=1):
	if len(set(group)) == 4:
		break

print(i + 3)

for i, group in enumerate(sliding_window(I, 14), start=1):
	if len(set(group)) == 14:
		break

print(i + 13)
