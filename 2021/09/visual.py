import curses
import sys
import argparse
from functools import reduce
from operator import mul


class Visual:

    def __init__(self, stdscr):
        curses.curs_set(0)
        try:
            curses.init_pair(1, curses.COLOR_WHITE, 124)
            curses.init_pair(2, curses.COLOR_WHITE, 130)
        except curses.error:
            args.color = False
        self.stdscr = stdscr
        self.pad = curses.newpad(110, 110)
        self.y, self.x = self.stdscr.getmaxyx()
        self.low_points = []
        self.total = []
        self.draw_grid()
        self.get_low_points()
        self.find_basins()
        result = str(reduce(mul, sorted(self.total)[-3:], 1))
        self.pad.addstr(101, 100//2 - (len(result) // 2), result, curses.A_REVERSE)
        self.stdscr.refresh()
        self.pad.refresh(0, 0, 0, 0, self.y - 1, self.x - 1)
        self.stdscr.getch()

    def draw_grid(self):
        self.pad.erase()
        y = 0
        for file_y, line in enumerate(input_file):
            self.pad.addstr(y, 0, "".join(str(c) for c in line))
            y += 1
        self.stdscr.refresh()
        self.pad.refresh(0, 0, 0, 0, self.y - 1, self.x - 1)

    def draw_low_point(self, c, color=False):
        if color and args.color:
            self.pad.addch(c[0], c[1], str(input_file[c[0]][c[1]]), curses.color_pair(color))
        else:
            self.pad.addch(c[0], c[1], str(input_file[c[0]][c[1]]), curses.A_REVERSE)
        self.stdscr.refresh()
        try:
            self.pad.refresh(c[0], c[1], c[0], c[1], self.y - 1, self.x - 1)
        except curses.error:
            self.pad.refresh(0, 0, 0, 0, self.y - 1, self.x - 1)

    def get_low_points(self):
        for y, l in enumerate(input_file):
            for x, i in enumerate(l):
                if (not y or input_file[y - 1][x] > i) \
                        and (y == len(input_file) - 1 or input_file[y + 1][x] > i):
                    if (not x or input_file[y][x - 1] > i) \
                            and (x == len(l) - 1 or input_file[y][x + 1] > i):
                        self.low_points.append((y, x))
                        self.draw_low_point((y, x), 1)

    def check_pos(self, y, x):
        aux = []
        if y and input_file[y - 1][x] != 9:
            aux.append((y - 1, x))
        if y < len(input_file) - 1 and input_file[y + 1][x] != 9:
            aux.append((y + 1, x))
        if x and input_file[y][x - 1] != 9:
            aux.append((y, x - 1))
        if x < len(input_file[y]) - 1 and input_file[y][x + 1] != 9:
            aux.append((y, x + 1))
        return aux

    def find_basins(self):
        t = set()
        for c in self.low_points:
            y, x = c
            b = set()
            b.add(c)
            aux = self.check_pos(y, x)
            for c in aux:
                b.add(c)
                t.add(c)
                self.draw_low_point(c, 2)
            prev = 0
            while True:
                aux = []
                for c in b:
                    aux.extend(self.check_pos(c[0], c[1]))
                for c in aux:
                    if c not in t:
                        curses.napms(args.delay // 100)
                        if c in self.low_points:
                            self.draw_low_point(c, 1)
                        else:
                            self.draw_low_point(c, 2)
                    b.add(c)
                    t.add(c)
                if len(b) == prev:
                    break
                prev = len(b)
            self.total.append(len(b))
            curses.napms(args.delay)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--delay", type=int, default=10,
                            help="specify delay in ms, default is 10"),
        parser.add_argument("-c", "--color", action="store_true",
                            help="use colors in visualization")
        args = parser.parse_args()
        input_file = [[int(i) for i in l] for l in open("input").read().splitlines()]
        curses.wrapper(Visual)
    except KeyboardInterrupt:
        sys.exit(1)
