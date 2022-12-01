from fileinput import input

elves = [[] for _ in range(500)]
i = 0
for line in input():
	if line == "\n":
		i += 1
		continue
	elves[i].append(int(line))

elves.sort(key=sum, reverse=1)
print(sum(elves[0]))
print(sum([fuck for python in elves[:3] for fuck in python]))
