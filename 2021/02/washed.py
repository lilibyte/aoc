#!/usr/bin/python3.10

f = [l.strip().split() for l in __import__('fileinput').input(files=('input'))]

a = h = h2 = dp = dp2 = 0

for d in f:
    match d:
        case ["forward", v]:
            h, h2 = (x + int(v) for x in (h, h2))
            dp2 += int(v) * a
        case ["down", v]:
            dp, a = (x + int(v) for x in (dp, a))
        case ["up", v]:
            dp, a = (x - int(v) for x in (dp, a))

print(h * dp)
print(h2 * dp2)
