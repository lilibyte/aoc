from aoc import input
from toolz import juxt

f = [[int(i) for i in row] for row in input().strip().split("\n")]
X, Y = len(f[0]) - 1, len(f) - 1

def up(y, x):
	return max(f[i][x] for i in range(y)) < f[y][x]

def down(y, x):
	return max(f[i][x] for i in range(y+1, Y+1)) < f[y][x]

def left(y, x):
	return max(f[y][:x]) < f[y][x]

def right(y, x):
	return max(f[y][x+1:]) < f[y][x]

check = juxt(up, down, left, right)

def score(y, x):
	total = 1
	xranges = ((x+1,X+1), (x-1,-1,-1))
	for r in xranges:
		for s, i in enumerate(range(*r), start=1):
			if f[y][i] >= f[y][x]:
				break
		total *= s
	yranges = ((y-1,-1,-1), (y+1,Y+1))
	for r in yranges:
		for s, i in enumerate(range(*r), start=1):
			if f[i][x] >= f[y][x]:
				break
		total *= s
	return total

silver, gold = ((X+1)*2) + (2*(Y-1)), 0
for y, row in enumerate(f[1:-1], start=1):
	for x, col in enumerate(row[1:-1], start=1):
		silver += any(check(y, x))
		gold = max(gold, score(y, x))

print(silver)
print(gold)
