from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true", default=False)
parser.add_argument("input", nargs="*")
args = parser.parse_args()

f = [l for l in __import__('fileinput').input(files=args.input if len(args.input) > 0 else ("-", ))][0].strip()
y = tuple(map(int, f.split("=")[-1].split("..")))
x = (int((sp:=(f.split("=")[-2].split("..")))[0]), int(sp[1].split(",")[0]))
ta = (x, y)

maxes = []

def step():
    p[0] += v[0]
    p[1] += v[1]
    if v[0] < 0:
        v[0] += 1
    elif v[0] > 0:
        v[0] -= 1
    v[1] -= 1

for mx in range(-500, 501):
    for my in range(-500, 501):
        v = [mx, my]
        maxy = 0
        p = [0, 0]
        if args.verbose:
            print("[!] starting on initial velocity", v,
                  end="\r", flush=True)
        for _ in range(500):
            step()
            if p[1] > maxy:
                maxy = p[1]
            if p[0] >= ta[0][0] and p[0] <= ta[0][1]:
                if p[1] >= ta[1][0] and p[1] <= ta[1][1]:
                    maxes.append(maxy)
                    if args.verbose:
                        print("[+] found matching velocity", v,
                              "highest y was", maxy)
                    break

if args.verbose:
    print()
print(max(maxes))
print(len(maxes))
