f = [l.strip() for l in __import__('fileinput').input()]

p1 = p2 = 0

for i in f:
    for w in i.split(" | ")[-1].split():
        if len(w) in (2, 4, 3, 7):
            p1 += 1

print(p1)

format = {
    (0, 1, 2, 4, 5, 6): 0,
    (2, 5): 1,
    (0, 2, 3, 4, 6): 2,
    (0, 2, 3, 5, 6): 3,
    (1, 2, 3, 5): 4,
    (0, 1, 3, 5, 6): 5,
    (0, 1, 3, 4, 5, 6): 6,
    (0, 2, 5): 7,
    (0, 1, 2, 3, 4, 5, 6): 8,
    (0, 1, 2, 3, 5, 6): 9,
}

def map_segments(sp):
    d = {}
    for w in sorted(sp.split(), key=len):
        if len(w) == 2:
            for z in sp.split():
                if len(z) == 6 and (w[0] not in z or w[1] not in z):
                    if z.count(w[0]):
                        d[2] = w[1]
                        d[5] = w[0]
                    else:
                        d[2] = w[0]
                        d[5] = w[1]
                    break
        elif len(w) == 3:
            for c in w:
                if not (c == d[2] or c == d[5]):
                    d[0] = c
                    break
        elif len(w) == 4:
            w = w.replace(d[2], "").replace(d[5], "")
            for z in sp.split():
                if len(z) == 5 and d[5] not in z:
                    if z.count(w[0]):
                        d[1] = w[1]
                        d[3] = w[0]
                    else:
                        d[1] = w[0]
                        d[3] = w[1]
                    break
        elif len(w) == 5 and d[2] not in w:
            w = w.replace(d[0], "").replace(d[1], "")
            w = w.replace(d[3], "").replace(d[5], "")
            d[6] = w
        elif len(w) == 7:
            w = w.replace(d[0], "").replace(d[1], "")
            w = w.replace(d[2], "").replace(d[3], "")
            w = w.replace(d[5], "").replace(d[6], "")
            d[4] = w
    return d

for l in f:
    sp, _, ov = l.partition(" | ")
    keys = map_segments(sp)
    aux = ""
    for w in ov.split():
        aux += str(format[tuple(sorted(k for k, v in keys.items() if v in w))])
    p2 += int(aux)

print(p2)
