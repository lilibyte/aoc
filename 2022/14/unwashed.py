from aoc import input
from collections import defaultdict
from itertools import pairwise, count

f = input().strip().split("\n")

AIR = 0
SAND = 1
ROCK = 2
VOID = 0

cave = defaultdict(int)

for line in f:
	line = line.split(" -> ")
	for a, b in pairwise(line):
		x, y = a.split(",")
		x2, y2 = b.split(",")
		x, y, x2, y2 = int(x), int(y), int(x2), int(y2)
		VOID = max(VOID, y, y2)
		if x > x2:
			x, x2 = x2, x
		if y > y2:
			y, y2 = y2, y
		for i in range(x, x2+1):
			cave[y,i] = ROCK
		for i in range(y, y2+1):
			cave[i,x] = ROCK

cave2 = cave.copy()

def drop(y=0, x=500, bottom=VOID, cave=cave):
	while cave[y, x] == AIR:
		if y == bottom:
			if bottom == VOID:
				return VOID, x
		y += 1
	if cave[y, x-1] == AIR:
		y, x = drop(y, x-1, bottom=bottom, cave=cave)
	elif cave[y, x+1] == AIR:
		y, x = drop(y, x+1, bottom=bottom, cave=cave)
	else:
		y -= 1
	return y, x

for silver in count():
	y, x = drop()
	if y == VOID:
		break
	cave[y, x] = SAND

print(silver)

for i in range(-5000, 5001):
	cave2[VOID+2,i] = ROCK

for gold in count():
	y, x = drop(bottom=VOID+2, cave=cave2)
	cave2[y, x] = SAND
	if y == 0 and x == 500:
		break

print(gold+1)
