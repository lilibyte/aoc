from aoc import scan

gold = silver = 0
for a, b, c, d in scan(r"(\d+)-(\d+),(\d+)-(\d+)"):
	if (a >= c and b <= d) or (c >= a and d <= b):
		silver += 1
	if (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
		gold += 1

print(silver)
print(gold)
