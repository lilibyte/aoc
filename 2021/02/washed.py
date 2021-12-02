#!/usr/bin/python3.10

f = [l.strip().split() for l in __import__('fileinput').input(files=('input'))]

a = h = dp = dp2 = 0

for d in f:
    match d:
        case ["forward", v]:
            h += int(v)
            dp2 += int(v) * a
        case ["down", v]:
            dp, a = (x + int(v) for x in (dp, a))
        case ["up", v]:
            dp, a = (x - int(v) for x in (dp, a))

print(h * dp)
print(h * dp2)
