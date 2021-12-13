from collections import defaultdict

f = [(l.strip().split("-")) for l in __import__('fileinput').input()]
p = defaultdict(list)

for l, r in f:
    p[l].append(r)
    p[r].append(l)

t = 0

def dfs(current, visited):
    global t
    visited = visited.copy()
    # courtesy of No.84738641 <3 <3
    if current in visited and any(v >= 2 for v in visited.values()):
    # if current in visited:
        return
    if current == "end":
        t += 1
        return
    if current.islower():
        visited[current] += 1
        # visited.add(current)
    neighbors = p[current]
    for next in neighbors:
        if next == "start":
            continue
        dfs(next, visited)

for e in p["start"]:
    # visited = set()
    visited = defaultdict(int)
    dfs(e, visited)

print(t)
