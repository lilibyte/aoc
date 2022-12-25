from aoc import input

# Merry Christmas, /aocg/ <3

f = input().strip().split("\n")
decimal = 0
for line in f:
	line = "".join(reversed(line))
	num = 0
	place = 1
	for c in line:
		if c == "=":
			c = -2
		elif c == "-":
			c = -1
		else:
			c = int(c)
		num += c * place
		place *= 5
	decimal += num

SNAFU = []
while decimal:
	fuck = int(decimal % 5)
	if fuck > 2:
		SNAFU.append("=" if fuck - 5 == -2 else "-")
	else:
		SNAFU.append(int(decimal % 5))
	if fuck > 2:
		decimal += abs(fuck - 5)
	decimal //= 5

print("".join(str(i) for i in reversed(SNAFU)))
