from fileinput import input
from collections import defaultdict

cwd = None
dirs = defaultdict(lambda: {"parent": None, "total": 0, "ctotal": 0})
listing = False

def path(key):
	if dirs[key].get("parent") is None:
		return key
	if dirs[key].get("parent") == "/":
		return "/" + key
	return dirs[key]["parent"] + "/" + key
for line in input():
	line = line.strip()
	if line.startswith("$ cd"):
		mk = line[5:]
		if mk == "..":
			cwd = dirs[cwd]["parent"]
		else:
			dirs["/" if not cwd else cwd + "/" + mk]["parent"] = cwd
			cwd = "/" if not cwd else cwd + "/" + mk
		listing = False
	elif line.startswith("$ ls"):
		listing = True
	elif listing:
		sz, name = line.split()
		if sz == "dir":
			dirs[cwd + "/" + name]["parent"] = cwd
		else:
			sz = int(sz)
			dirs[cwd]["total"] += sz
			parent = dirs[cwd]["parent"]
			while parent is not None:
				dirs[parent]["ctotal"] += sz
				parent = dirs[parent]["parent"]

silver, gold = 0, 70000000
free = 30000000 - (gold - (dirs["/"]["total"] + dirs["/"]["ctotal"]))
for d in dirs:
	if dirs[d]["total"] + dirs[d]["ctotal"] <= 100000:
		silver += dirs[d]["total"] + dirs[d]["ctotal"]
	if dirs[d]["total"] + dirs[d]["ctotal"] >= free:
		gold = min(gold, dirs[d]["total"] + dirs[d]["ctotal"])

print(silver)
print(gold)
