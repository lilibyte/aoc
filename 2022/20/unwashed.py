from aoc import input
from collections import deque

ia = deque([*map(lambda x: (int(x), 0), input().strip().split())])
order = [[i[0] * 811589153] for i in ia]
ia2 = deque(order)

for _ in range(len(ia)):
	n, m = ia.popleft()
	while m:
		ia.insert(0, (n, m))
		ia.rotate(-1)
		n, m = ia.popleft()
	ia.insert((n % len(ia) - len(ia)), (n, 1))

z = ia.index((0, 1)) - len(ia)
silver = sum(ia[z + i % len(ia)][0] for i in (1000, 2000, 3000))
print(silver)

for r in range(1, 10+1):
	for i in range(len(ia2)):
		n = ia2.popleft()
		while n is not order[i]:
			ia2.insert(0, n)
			ia2.rotate(-1)
			n = ia2.popleft()
		ia2.insert((n[0] % len(ia2) - len(ia2)), n)

z = ia2.index([0]) - len(ia2)
gold = sum(ia2[z + i % len(ia2)][0] for i in (1000, 2000, 3000))
print(gold)
