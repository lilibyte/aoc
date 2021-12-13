from collections import defaultdict
f = [l for l in open(0).read().split("\n\n")]
ds = [l.split(",") for l in f[0].split("\n")]
ds = [(int(x), int(y)) for x, y in ds]
fi = [l.split(" ")[-1].split("=") for l in f[1].split("\n") if l.strip()]
fi = [(c, int(i)) for c, i in fi if i and c]
maxx, maxy, tp = 0, 0, defaultdict(int)

for c in ds:
    maxx = max(c[0], maxx)
    maxy = max(c[1], maxy)
    tp[(c[0], c[1])] = 1

def fold(d, n):
    global maxx, maxy
    mx = maxy if d == "y" else maxx
    for c in tp.copy():
        cc = c[1] if d == "y" else c[0]
        if cc > n % mx:
            newc = abs(cc - (n % mx) * 2)
            newc = (c[0], newc) if d == "y" else (newc, c[1])
            tp[newc] += 1
            del tp[c]
    if d == "y":
        maxy -= (n - 1)
    else:
        maxx -= (n - 1)

def draw_paper():
    for y in range(maxy+1):
        for x in range(maxx+1):
            print("█" if (x, y) in tp else " ", end="")
        print()

for c, i in enumerate(fi, start=1):
    fold(*i)
    if c == 1:
        print(len(tp))
    if c == len(fi):
        draw_paper()
