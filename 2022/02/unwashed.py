from aoc import scan

defeats  = {"A": 3, "B": 1, "C": 2}
defeated = {"A": 2, "B": 3, "C": 1}

def rps(a, b):
	return (3 + a - b) % 3

p2 = p1 = 0
for a, b in scan(r"(\w) (\w)"):
	r = rps(ord(a) - ord("A"), ord(b) - ord("X"))
	p1 += ord(b)-(ord("X")-1)
	if r == 0:
		p1 += 3
	elif r == 2:
		p1 += 6
	if b == "Y":
		p2 += (ord(a)-(ord("A")-1)) + 3
	elif b == "X":
		p2 += defeats[a]
	elif b == "Z":
		p2 += defeated[a] + 6

print(p1)
print(p2)
