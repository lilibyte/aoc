#!/usr/bin/python3.10

import curses
import sys
import argparse
import fileinput
import random
import collections


sub_left = r"""           o
  _|______/|
 /          \/\
( )\\\\___  =|>
 \____ (___)/\/
,/,/       \|
            o"""


sub_right = r"""   o
   |\______|_
/\/          \
<|=  ___////( )
\/\(___) ____/
  |/       \,\,
  o"""

whale = """                          .
                         ==
                        ===
   /"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"___/ ===
  {                      /  ===-
   \\______ o          __/
    \\    \\        __/
      \\____\\______/"""

fishe_left = "<><"
fishe_right = "><>"
big_fishe_left = "<°))))><"
big_fishe_right = "><(((°>"

# a
shark_right = r"""      .
\_____)\_____
/--v____ __`<
        )/
        '"""


# a
shark_left = r"""      .
_____/(_____/
>'__ ____v--\
   \(
    `"""

class Visual:

    def __init__(self, stdscr):
        curses.curs_set(0)
        self.stdscr = stdscr
        self.stdscr.nodelay(1)
        self.h, self.w = self.stdscr.getmaxyx()
        self.depth = self.horiz = self.aim = 0
        self.sub_pos_y = 1
        self.sub_pos_x = 0
        # might have to play with these values to get it to play
        # nicely on different sized terminals
        self.d_limit = 4 if self.w > 200 else 10
        self.h_limit = 4 if self.h > 100 else 10
        # self.d_limit = 4 if self.w > 200 else 5
        # self.h_limit = 2 if self.h > 100 else 10
        self.chart_pos = []
        self.critter_pos = collections.defaultdict(list)
        self.prev = ""
        if args.critters:
            self.determine_critter_pos()
        for line in input_file:
            match line:
                case ["forward", v]:
                    self.horiz += int(v)
                    self.depth += int(v) * self.aim
                case ["down", v]:
                    self.aim += int(v)
                case ["up", v]:
                    self.aim -= int(v)
            self.line = " ".join(line)
            self.show()
            self.getch()
            curses.napms(args.delay)
        total = self.horiz * self.depth
        total_str = f" horizontal * depth == {total} "
        self.stdscr.addstr(self.h // 2, (self.w // 2) - len(total_str) // 2,
                           total_str, curses.A_REVERSE)
        self.stdscr.nodelay(0)
        self.getch()

    def show(self):
        self.stdscr.erase()

        # draw counters to screen
        self.stdscr.addstr(0, 1, f"h_pos: {self.horiz}")
        self.stdscr.addstr(0, 20, f"depth: {self.depth}")
        self.stdscr.addstr(0, 40, f"aim: {self.aim}")
        self.stdscr.addstr(0, 60, f"cmd: {self.line}\n")

        # draw critters to screen if enabled
        if args.critters:
            for pos in self.critter_pos["fishe_left"]:
                self.stdscr.addstr(pos[0], pos[1], fishe_left)
            for pos in self.critter_pos["fishe_right"]:
                self.stdscr.addstr(pos[0], pos[1], fishe_right)
            for pos in self.critter_pos["big_fishe_left"]:
                self.stdscr.addstr(pos[0], pos[1], big_fishe_left)
            for pos in self.critter_pos["big_fishe_right"]:
                self.stdscr.addstr(pos[0], pos[1], big_fishe_right)
            for pos in self.critter_pos["shark_left"]:
                if pos:
                    i = 0
                    for line in shark_left.splitlines():
                        self.stdscr.addstr(pos[0] + i, pos[1], line)
                        i += 1
            for pos in self.critter_pos["shark_right"]:
                if pos:
                    i = 0
                    for line in shark_right.splitlines():
                        self.stdscr.addstr(pos[0] + i, pos[1], line)
                        i += 1
            for pos in self.critter_pos["whale"]:
                if pos:
                    i = 0
                    for line in whale.splitlines():
                        self.stdscr.addstr(pos[0] + i, pos[1], line)
                        i += 1

        # set options for increasing horizontal position
        if self.line.startswith("f") and not self.horiz % self.h_limit \
           and self.sub_pos_x < self.w - 15:
            char = "⠈" if self.prev == "down" else "⠒"
            self.chart_pos.append([self.sub_pos_y + 3, self.sub_pos_x, char])
            self.sub_pos_x += 1
            self.prev = "forward"

        # draw sub to screen
        for line in sub_right.splitlines():
            self.stdscr.addstr(self.sub_pos_y, self.sub_pos_x, line)
            if self.sub_pos_y + 1 < self.h:
                self.sub_pos_y += 1

        # sub will return to its prior position
        self.sub_pos_y -= 7

        # set options for increasing depth
        if self.line.startswith("d") and not self.depth % self.d_limit:
            char = "⢢" if self.prev == "forward" else "⢸"
            self.chart_pos.append([self.sub_pos_y + 3, self.sub_pos_x, char])
            self.sub_pos_y += 1
            self.prev = "down"

        # draw lines to screen if enabled
        if args.lines:
            for pos in self.chart_pos:
                self.stdscr.addstr(pos[0], pos[1], pos[2])

        self.stdscr.refresh()

    def getch(self):
        match self.stdscr.getch():
            case curses.KEY_RESIZE:
                self.h, self.w = self.stdscr.getmaxyx()
            case 113:
                sys.exit(0)

    def determine_critter_pos(self):
        for i in range(self.w // 25):
            self.critter_pos["fishe_left"].append((random.randint(2, self.h - 5), random.randint(2, self.w - 5)))
        for i in range(self.w // 25):
            self.critter_pos["fishe_right"].append((random.randint(2, self.h - 5), random.randint(2, self.w - 5)))
        for i in range(random.randint(0, 4)):
            self.critter_pos["big_fishe_left"].append((random.randint(2, self.h - 5), random.randint(2, self.w - 12)))
        for i in range(random.randint(0, 4)):
            self.critter_pos["big_fishe_right"].append((random.randint(2, self.h - 5), random.randint(2, self.w - 12)))
        for i in range(random.randint(0, 2)):
            self.critter_pos["shark_left"].append((random.randint(2, self.h - 5), random.randint(2, self.w - 12)))
        for i in range(random.randint(0, 3)):
            self.critter_pos["shark_right"].append((random.randint(2, self.h - 5), random.randint(2, self.w - 12)))
        for i in range(bool(random.getrandbits(1))):
            self.critter_pos["whale"].append((random.randint(2, self.h - 10), random.randint(2, self.w - 20)))


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("input", help="input file, defaults to stdin")
        parser.add_argument("-d", "--delay", type=int, default=10,
                            help="delay in miliseconds, defaults to 10")
        parser.add_argument("-l", "--lines", action="store_true", default=True,
                            help="draw line behind submarine")
        parser.add_argument("-c", "--critters", action="store_true", default=False,
                            help="draw cute sea friends")
        args = parser.parse_args()
        input_file = [l.strip().split() for l in fileinput.input(files=args.input)]
        curses.wrapper(Visual)
    except KeyboardInterrupt:
        sys.exit(1)
