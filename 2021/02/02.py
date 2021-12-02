f = [l.strip() for l in __import__('fileinput').input(files=('input'))]

h = 0
dp = 0

for l in f:
    d, i = l.split()
    i = int(i)
    if d == "forward":
        h += i
    elif d == "down":
        dp += i
    elif d == "up":
        dp -= i

print(h * dp)


h = 0
dp = 0
a = 0

for l in f:
    d, i = l.split()
    i = int(i)
    if d == "forward":
        h += i
        dp += i * a
    elif d == "down":
        a += i
    elif d == "up":
        a -= i

print(h * dp)
