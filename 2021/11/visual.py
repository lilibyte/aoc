import curses
import sys
import argparse
import itertools
import time


class Visual:

    def __init__(self, stdscr):
        curses.curs_set(0)
        self.f = [[int(i) for i in l.strip()] for l in open("test")]
        self.stdscr = stdscr
        self.i = self.p1 = 0
        for y, l in enumerate(self.f):
            self.stdscr.addstr(y, 0, "".join(str(c) for c in l))
        self.stdscr.addstr(y + 2, 0, str(self.p1))
        self.stdscr.addstr(y + 3, 0, str(self.i))
        self.stdscr.refresh()
        curses.napms(args.delay)
        time.sleep(5)
        while True:
            if not sum(1 for e in itertools.chain(*self.f) if e != 0):
                if self.i > args.min:
                    break
            self.stdscr.erase()
            self.af = set()
            for y, l in enumerate(self.f):
                for x, o in enumerate(l):
                    if o < 9 and (y, x) not in self.af:
                        self.f[y][x] += 1
                        self.stdscr.addch(y, x, str(self.f[y][x]))
                    elif o == 9:
                        self.flash(y, x)
            self.i += 1
            self.stdscr.addstr(y + 2, 0, str(self.p1))
            self.stdscr.addstr(y + 3, 0, str(self.i))
            self.stdscr.refresh()
            curses.napms(args.delay)
        self.stdscr.addstr(y + 2, 0, str(self.p1))
        self.stdscr.addstr(y + 3, 0, str(self.i))
        self.stdscr.getch()

    def flash(self, y, x):
        if (y, x) in self.af:
            return
        self.af.add((y, x))
        self.f[y][x] = 0
        self.stdscr.addch(y, x, str(self.f[y][x]), curses.A_REVERSE)

        if self.i < args.min:
            self.p1 += 1
        if y:
            if self.f[y - 1][x] < 9 and (y - 1, x) not in self.af:
                self.f[y - 1][x] += 1
                self.stdscr.addch(y - 1, x, str(self.f[y - 1][x]))
            else:
                self.flash(y - 1, x)
        if y < len(self.f) - 1:
            if self.f[y + 1][x] < 9 and (y + 1, x) not in self.af:
                self.f[y + 1][x] += 1
                self.stdscr.addch(y + 1, x, str(self.f[y + 1][x]))
            else:
                self.flash(y + 1, x)
        if x:
            if self.f[y][x - 1] < 9 and (y, x - 1) not in self.af:
                self.f[y][x - 1] += 1
                self.stdscr.addch(y, x - 1, str(self.f[y][x - 1]))
            else:
                self.flash(y, x - 1)
        if x < len(self.f[y]) - 1:
            if self.f[y][x + 1] < 9 and (y, x + 1) not in self.af:
                self.f[y][x + 1] += 1
                self.stdscr.addch(y, x + 1, str(self.f[y][x + 1]))
            else:
                self.flash(y, x + 1)
        if y and x:
            if self.f[y - 1][x - 1] < 9 and (y - 1, x - 1) not in self.af:
                self.f[y - 1][x - 1] += 1
                self.stdscr.addch(y - 1, x - 1, str(self.f[y - 1][x - 1]))
            else:
                self.flash(y - 1, x - 1)
        if y < len(self.f) - 1 and x:
            if self.f[y + 1][x - 1] < 9 and (y + 1, x - 1) not in self.af:
                self.f[y + 1][x - 1] += 1
                self.stdscr.addch(y + 1, x - 1, str(self.f[y + 1][x - 1]))
            else:
                self.flash(y + 1, x - 1)
        if y and x < len(self.f[y]) - 1:
            if self.f[y - 1][x + 1] < 9 and (y - 1, x + 1) not in self.af:
                self.f[y - 1][x + 1] += 1
                self.stdscr.addch(y - 1, x + 1, str(self.f[y - 1][x + 1]))
            else:
                self.flash(y - 1, x + 1)
        if y < len(self.f) - 1 and x < len(self.f[y]) - 1:
            if self.f[y + 1][x + 1] < 9 and (y + 1, x + 1) not in self.af:
                self.f[y + 1][x + 1] += 1
                self.stdscr.addch(y + 1, x + 1, str(self.f[y + 1][x + 1]))
            else:
                self.flash(y + 1, x + 1)

        self.stdscr.refresh()


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--delay", type=int, default=100,
                            help="specify delay in ms, default is 100"),
        parser.add_argument("-m", "--min", type=int, default=100,
                            help="minimum iterations (part 1), default 100")
        args = parser.parse_args()
        curses.wrapper(Visual)
    except KeyboardInterrupt:
        sys.exit(1)
