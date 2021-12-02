#!/usr/bin/python3.10

f = [l.strip() for l in __import__('fileinput').input(files=('input'))]

a = h = h2 = dp = dp2 = 0

for l in f:
    d, i = l.split()[0], int(l.split()[1])
    match d:
        case "forward":
            h, h2 = (x + i for x in (h, h2))
            dp2 += i * a
        case "down":
            dp, a = (x + i for x in (dp, a))
        case "up":
            dp, a = (x - i for x in (dp, a))

print(h * dp)
print(h2 * dp2)
