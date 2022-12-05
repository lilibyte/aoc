import curses
from aoc import input
from collections import deque

CRATES = 9
RANGE = 34

class Visual:

	def __init__(self, stdscr):
		curses.curs_set(0)
		self.stdscr = stdscr
		I = input().split("\n")
		C = I[:CRATES-1]
		self.crates = [deque() for _ in range(CRATES)]
		self.ins = I[CRATES+1:len(I)-1]
		for line in C:
			for c, i in enumerate(range(1, RANGE + 3, 4)):
				if line[i] != " ":
					self.crates[c].append(line[i])
		self.draw(0)
		self.run()
		self.stdscr.addstr(41, 0, "".join(crate[0] for crate in self.crates if crate).ljust(30, " "))
		self.stdscr.refresh()
		self.stdscr.getch()

	def draw(self, line):
		self.stdscr.erase()
		col = 1
		for crate in self.crates:
			row = 39 - len(crate)
			for c, letter in enumerate(crate):
				self.stdscr.addstr(row, col, f"[{letter}]")
				row += 1
			col += 4
		self.stdscr.addstr(39, 0, "  1   2   3   4   5   6   7   8   9")
		for x, i in enumerate(self.ins[line:line+6]):
			self.stdscr.addstr(41 + x, 0, i)
		self.stdscr.refresh()

	def run(self):
		for i, op in enumerate(self.ins):
			op = op.split()
			n = int(op[1])
			fr = int(op[3])
			to = int(op[5])
			for _ in range(n):
				self.crates[to-1].appendleft(self.crates[fr-1].popleft())
				self.draw(i)
				curses.napms(3)

if __name__ == "__main__":
	try:
		curses.wrapper(Visual)
	except KeyboardInterrupt:
		exit(1)
