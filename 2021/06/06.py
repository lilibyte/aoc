from functools import lru_cache
lf = [int(i) for i in open("input").read().strip().split(",")]

@lru_cache(2048)
def r(t, s=0):
    f = 0
    for i in range(s, 256):
        if not t:
            t = 7
            f += 1
            f += r(8, i+1)
        t -= 1
    return f

print(sum(r(i) for i in lf) + len(lf))
