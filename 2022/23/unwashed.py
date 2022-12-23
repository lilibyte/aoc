from aoc import input
from collections import deque, defaultdict
from itertools import count

f = input().strip().split("\n")
directions = deque([
	(((-1, 0), (-1, 1), (-1, -1)), (-1, 0)),
	(((1, 0), (1, 1), (1, -1)), (1, 0)),
	(((0, -1), (-1, -1), (1, -1)), (0, -1)),
	(((0, 1), (-1, 1), (1, 1)), (0, 1))])
offset = 1000
elves = defaultdict(int)
for y, row in enumerate(f, start=offset):
	for x, col in enumerate(row):
		if col == "#":
			elves[y, x] = 1

for round in count(1):
	if round == 11:
		junk = sorted(elves.keys(), key=lambda x: x[0])
		miny, maxy = junk[0][0], junk[-1][0]
		junk = sorted(elves.keys(), key=lambda x: x[1])
		minx, maxx = junk[0][1], junk[-1][1]
		silver = ((maxx - minx) + 1) * ((maxy - miny) + 1)
		for y, x in elves:
			if y >= miny and y <= maxy and x >= minx and x <= maxx:
				silver -= 1
		print(silver)
	remaining = defaultdict(int)
	propositions = defaultdict(int)
	for elf in elves:
		ey, ex = elf
		start = directions.copy()
		for dirs, res in start:
			if any(elves.get((ey + y, ex + x)) for y, x in dirs):
				break
		else:
			continue
		for dirs, res in start:
			if not any(elves.get((ey + y, ex + x)) for y, x in dirs):
				p = (ey + res[0], ex + res[1])
				remaining[elf] = p
				propositions[p] += 1
				break
	kill = True
	for elf in remaining:
		if propositions[remaining[elf]] == 1:
			del elves[elf]
			elves[remaining[elf]] = 1
			kill = False
	if kill:
		print(round)
		break
	directions.rotate(-1)
