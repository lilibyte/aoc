from aoc import input
from collections import namedtuple, defaultdict, deque

f = input().strip().split("\n")
Vertex = namedtuple("Vertex", ["y", "x", "cost"])
Edge = namedtuple("Edge", ["top", "right", "bottom", "left"])
tmp = [bytearray(len(f[0])) for _ in range(len(f))]
heights = defaultdict(lambda: None)

for y, row in enumerate(f):
	for x, col in enumerate(row):
		if col == "S":
			start = Vertex(y, x, 1)
			tmp[y][x] = 1
		elif col == "E":
			dest = Vertex(y, x, 26)
			tmp[y][x] = 26
		else:
			tmp[y][x] = ord(col) - (ord("a")-1)

for y, row in enumerate(tmp):
	for x, col in enumerate(row):
		top = None
		right = None
		bottom = None
		left = None
		if y:
			top = Vertex(y-1, x, tmp[y-1][x])
		if y < len(tmp)-1:
			bottom = Vertex(y+1, x, tmp[y+1][x])
		if x:
			left = Vertex(y, x-1, row[x-1])
		if x < len(row)-1:
			right = Vertex(y, x+1, row[x+1])
		heights[Vertex(y, x, col)] = Edge(top, right, bottom, left)

def bfs(start, dest):
	q = deque()
	visited = set()
	visited.add(start)
	q.append((start, 0))
	while q:
		node, length = q.popleft()
		if node == dest:
			return length + 1
		for neighbor in heights[node]:
				if neighbor is None or neighbor.cost > node.cost + 1:
					continue
				if neighbor not in visited:
					visited.add(neighbor)
					q.append((neighbor, length + 1))

print(bfs(start, dest) - 1)

all_a = set()
for y, row in enumerate(f):
	for x, col in enumerate(row):
		if col == "a":
			r = bfs(Vertex(y, x, 1), dest)
			if r is not None:
				all_a.add(r - 1)

print(min(all_a))
