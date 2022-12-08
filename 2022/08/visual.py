"""
Lighter green means more directions the tree is visible from
outside the grid.

Trees on the edge are set to the lightest shade.

Scroll down:               j or down arrow
Scroll up:                 k or up arrow
Scroll left:               h or left arrow
Scroll right:              l or right arrow
Scroll to the top:         g or page up
Scroll to the bottom:      G or page down
Scroll to the left edge:   _
Scroll to the right edge:  $
Quit:                      q or Q or Z or Ctrl+c
"""

import curses
from fileinput import input

f = [[int(i) for i in row] for row in "".join(input()).strip().split("\n")]
X, Y = len(f[0]) - 1, len(f) - 1

def up(y, x):
	return not y or max(f[i][x] for i in range(y)) < f[y][x]

def down(y, x):
	return y == Y or max(f[i][x] for i in range(y+1, Y+1)) < f[y][x]

def left(y, x):
	return not x or max(f[y][:x]) < f[y][x]

def right(y, x):
	return x == X or max(f[y][x+1:]) < f[y][x]

def check(y, x):
	return (up(y, x), down(y, x), left(y, x), right(y, x))

class Visual:

	def __init__(self, stdscr):
		curses.curs_set(0)
		curses.init_pair(10, 94, 22)
		curses.init_pair(11, 94, 34)
		curses.init_pair(12, 94, 46)
		curses.init_pair(13, 94, 82)
		curses.init_pair(14, 94, 118)
		self.stdscr = stdscr
		self.stdscr.nodelay(1)
		self.my, self.mx = self.stdscr.getmaxyx()
		self.y, self.x = 0, 0
		self.pad = curses.newpad(Y+10,X+10)
		self.draw(init=True)
		self.stdscr.refresh()
		self.pad.refresh(self.y,self.x, 0,0, self.my-1, self.mx-1)
		while True:
			self.draw()

	def draw(self, init=False):
		for y, row in enumerate(f):
			for x, col in enumerate(row):
				v = sum(check(y, x))
				if not y or not x:
					self.pad.addstr(y, x, str(col), curses.color_pair(14))
				elif x == X or y == Y:
					self.pad.addstr(y, x, str(col), curses.color_pair(14))
				else:
					self.pad.addstr(y, x, str(col), curses.color_pair(10 if init else 10+v))
				if not init:
					self.getkey()
					self.stdscr.refresh()
					self.pad.refresh(self.y,self.x, 0,0, self.my-1, self.mx-1)
					curses.napms(1)

	def getkey(self):
		c = self.stdscr.getch()
		if c in (ord("q"), ord("Q"), ord("Z")):
			exit(0)
		elif c == curses.KEY_RESIZE:
			self.my, self.mx = self.stdscr.getmaxyx()
		elif c in (ord("j"), curses.KEY_DOWN):
			self.y = min(Y-self.my+1, self.y + 1)
		elif c in (ord("k"), curses.KEY_UP):
			self.y = max(0, self.y - 1)
		elif c in (ord("h"), curses.KEY_LEFT):
			self.x = max(0, self.x - 1)
		elif c in (ord("l"), curses.KEY_RIGHT):
			self.x = min(X-self.mx+1, self.x + 1)
		elif c in (ord("g"), curses.KEY_PPAGE):
			self.y = 0
		elif c in (ord("G"), curses.KEY_NPAGE):
			self.y = Y-self.my+1
		elif c in (ord("$"),):
			self.x = X-self.mx+1
		elif c in (ord("_"),):
			self.x = 0

if __name__ == "__main__":
	try:
		curses.wrapper(Visual)
	except KeyboardInterrupt:
		exit(1)
