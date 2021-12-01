f = [int(l.strip()) for l in __import__('fileinput').input(files=('input'))]
la = 0
t = 0

for c, l in enumerate(f):
    if l > la and c:
        t += 1
    la = l

print(t)

ps = 0
t = 0

for i in range(c):
    cs = sum(f[i:i+3])
    if ps and cs > ps:
        t += 1
    ps = cs

print(t)
