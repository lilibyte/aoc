from fileinput import input

last3 = [set(), set(), set()]
p2 = p1 = 0
i = 1
for line in input():
	line = line.strip()
	a, b = set(line[:len(line)//2]), (line[len(line)//2:])
	c = a.intersection(b)
	for letter in c:
		if ord(letter) >= ord("a"):
			p1 += ord(letter) - (ord("a") - 1)
		else:
			p1 += ord(letter) - (ord("A") - 1) + 26
	last3[i % 3] = set(line)
	if i % 3 == 0:
		c = last3[0].intersection(last3[1], last3[2])
		letter = list(c)[0]
		if ord(letter) >= ord("a"):
			p2 += ord(letter) - (ord("a") - 1)
		else:
			p2 += ord(letter) - (ord("A") - 1) + 26
	i += 1

print(p1)
print(p2)
