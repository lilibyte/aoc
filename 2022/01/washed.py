from aoc import input

elves = [*map(lambda l: [*map(int, l.split())], input().split("\n\n"))]
elves.sort(key=sum, reverse=1)
print(sum(elves[0]))
print(sum([n for elf in elves[:3] for n in elf]))
