f = [[int(i) for i in l.strip()] for l in __import__('fileinput').input()]

p1 = 0

def fl(y, x):
    global p1
    if (y, x) in af:
        return
    af.add((y, x))
    f[y][x] = 0
    if i < 100:
        p1 += 1
    if y:
        if f[y - 1][x] < 9:
            if (y - 1, x) not in af:
                f[y - 1][x] += 1
        else:
            fl(y - 1, x)
    if y < len(f) - 1:
        if f[y + 1][x] < 9:
            if (y + 1, x) not in af:
                f[y + 1][x] += 1
        else:
            fl(y + 1, x)
    if x:
        if f[y][x - 1] < 9:
            if(y, x - 1) not in af:
                f[y][x - 1] += 1
        else:
            fl(y, x - 1)
    if x < len(f[y]) - 1:
        if f[y][x + 1] < 9:
            if (y, x + 1) not in af:
                f[y][x + 1] += 1
        else:
            fl(y, x + 1)
    if y and x:
        if f[y - 1][x - 1] < 9:
            if (y - 1, x - 1) not in af:
                f[y - 1][x - 1] += 1
        else:
            fl(y - 1, x - 1)
    if y < len(f) - 1 and x:
        if f[y + 1][x - 1] < 9:
            if (y + 1, x - 1) not in af:
                f[y + 1][x - 1] += 1
        else:
            fl(y + 1, x - 1)
    if y and x < len(f[y]) - 1:
        if f[y - 1][x + 1] < 9:
            if (y - 1, x + 1) not in af:
                f[y - 1][x + 1] += 1
        else:
            fl(y - 1, x + 1)
    if y < len(f) - 1 and x < len(f[y]) - 1:
        if f[y + 1][x + 1] < 9:
            if (y + 1, x + 1) not in af:
                f[y + 1][x + 1] += 1
        else:
            fl(y + 1, x + 1)

i = 0
while True:
    af = set()
    s = 0
    for y, l in enumerate(f):
        if l.count(0) == len(l):
            s += 1
        for x, o in enumerate(l):
            if o < 9 and (y, x) not in af:
                f[y][x] += 1
            elif o == 9:
                fl(y, x)
    if s == len(f):
        print("part 2:", i)
        if i > 100:
            break
    i += 1
    s = 0

print("part 1:", p1)
