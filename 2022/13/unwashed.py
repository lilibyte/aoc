from aoc import input
from itertools import zip_longest
from more_itertools import flatten

f = input().strip().split("\n\n")
packets = [[eval(subline) for subline in pair.split("\n")] for pair in f]

def packetcmp(a, b):
	if isinstance(a, int) and isinstance(b, int):
		if a == b:
			return 0
		if a < b:
			return -1
		return 1
	elif isinstance(a, list) and isinstance(b, list):
		for c, d in zip_longest(a, b):
			r = packetcmp(c, d)
			if r == 0:
				continue
			return r
		return 0
	elif isinstance(a, list) and isinstance(b, int):
		return packetcmp(a, [b])
	elif isinstance(a, int) and isinstance(b, list):
		return packetcmp([a], b)
	elif a is None and b is not None:
		return -1
	elif a is not None and b is None:
		return 1

silver = 0
for i, packet in enumerate(packets, start=1):
	for a, b in zip_longest(*packet):
		match packetcmp(a, b):
			case 0:
				continue
			case -1:
				silver += i
				break
			case 1:
				break

print(silver)

def bubble_sort(lst):
	cont = True
	while cont:
		cont = False
		for i in range(len(lst)-1):
			if packetcmp(lst[i], lst[i+1]) == -1:
				lst[i], lst[i+1] = lst[i+1], lst[i]
				cont = True
	lst.reverse()

packets.extend([[[2]], [[6]]])
packets = list(flatten(packets))
bubble_sort(packets)
print((packets.index([2])+1) * (packets.index([6])+1))
