from aoc import input
from collections import defaultdict

f = input().strip().split("\n")
N = defaultdict(int)
buffer, buffer2 = set(), set()

for line in f:
	monkey, op = line.split(": ")
	op = op.split()
	if len(op) == 1:
		N[monkey] = int(op[0])
	else:
		buffer.add(tuple((monkey, *op)))
		if monkey == "root":
			a, _, b = op
			buffer2.add(tuple((monkey, a, "==", b)))
		else:
			buffer2.add(tuple((monkey, *op)))

N2 = N.copy()

while buffer:
	for line in buffer.copy():
		monkey, a, op, b = line
		if N.get(a) is None or N.get(b) is None:
			continue
		buffer.remove(line)
		N[monkey] = eval(f"{N[a]} {op} {N[b]}")

print(int(N["root"]))

# part 2 solved by pure manual trial and error. i tried to use
# binary sort kinda logic to create a folding window of possible
# answers, but didn't get it to work and then realized i could
# just keep changing the humn number until it got close to its
# goal.
# i used the upper/lower bounds logic from my folding attempt
# as a starting place for what to set humn to manually.

# not sure this counts as a solution but it's surely "unwashed"

# 3305669217845 too high ???
fuck = N2.copy()
fuck["root"] = 0
# n = 3305669222222
n = 3305669217845
hmm = 0
kill = solved = False
while not fuck["root"] or not kill:
	N2["humn"] = n
	fuck = N2.copy()
	buffer = buffer2.copy()
	while buffer:
		for line in buffer.copy():
			monkey, a, op, b = line
			if fuck.get(a) is None or fuck.get(b) is None:
				continue
			buffer.remove(line)
			fuck[monkey] = eval(f"int({fuck[a]}) {op} int({fuck[b]})")
	# subtracting for a < b and adding for a > b is input dependent i think
	if fuck[a] < fuck[b]:
		if solved:
			kill = True
		# upper_bounds = min(n, upper_bounds)
		# n -= upper_bounds // 2
		# # n = max(n, lower_bounds + 1)
		n -= 1
	elif fuck[a] > fuck[b]:
		if solved:
			kill = True
		# lower_bounds = max(n, lower_bounds)
		# n += upper_bounds // 2
		# n += n // 4
		# n += upper_bounds // 4
		# # n = min(n, upper_bounds - 1)
		n += 1
	# otherwise it'll break the first time it gets a correct
	# answer, and AoC only accepted the lowest one
	else:
		n -= 1
		solved = True
	print(int(fuck[a]), fuck[b], n, int(fuck[a]) - int(fuck[b]))

print(N2["humn"])
