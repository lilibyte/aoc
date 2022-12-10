from aoc import input

# fuuuuuuuucking tired of python
ins = [[line.split()[0], int(0 if line[0] == "n" else line.split()[-1])] for line in input().strip().split("\n") if line]

C = [20, 60, 100, 140, 180, 220]
CRT = [bytearray(40) for _ in range(6)]
X = cycle = 1
silver = 0

def draw():
	c = (cycle-1) % 40
	if c >= X - 1 and c <= X + 1:
		CRT[(cycle-1) // 40][c] = 1

def inc():
	global cycle, silver
	cycle += 1
	if cycle in C:
		silver += (cycle * X)
		C.remove(cycle)

for op, n in ins:
	draw()
	match op:
		case "noop":
			inc()
		case "addx":
			inc()
			draw()
			X += n
			inc()

print(silver)
print("\n".join("".join("░" if i else "▓" for i in row) for row in CRT))
