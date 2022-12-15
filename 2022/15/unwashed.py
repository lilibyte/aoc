from aoc import scan
from collections import namedtuple, defaultdict

Y = 2000000
M = 4000000

Point = namedtuple("Point", ["y", "x"])

sensors = defaultdict(Point)
beacons = defaultdict(Point)

def manhattan(p, q):
	return abs(p.x - q.x) + abs(p.y - q.y)

for line in scan(r"[^\d-]*(-?\d+)[^\d-]*(-?\d+)[^\d-]*(-?\d+)[^\d-]*(-?\d+)"):
	sensors[Point(line[1], line[0])] = Point(line[3], line[2])
	beacons[Point(line[3], line[2])] = Point(line[1], line[0])

not_beacons = set()

for sensor in sensors:
	dist = manhattan(sensor, sensors[sensor])
	above = Y >= sensor.y - dist and Y <= sensor.y
	below = Y >= sensor.y and Y <= sensor.y + dist
	if above or below:
		a = (sensor.x - dist) + abs(Y - sensor.y)
		b = (sensor.x + dist) - abs(Y - sensor.y)
		not_beacons.add((a, b))

not_beacons = sorted(not_beacons)
a = not_beacons[0][0]
not_beacons = sorted(not_beacons, key=lambda x: x[1])
b = not_beacons[-1][1]

silver = abs(a) + abs(b) + 1
for beacon in beacons:
	if beacon.y == Y and beacon.x >= a and beacon.x <= b:
		silver -= 1

print(silver)

for Y in range(M+1):
	not_beacons = set()
	for sensor in sensors:
		dist = manhattan(sensor, sensors[sensor])
		above = Y >= sensor.y - dist and Y <= sensor.y
		below = Y >= sensor.y and Y <= sensor.y + dist
		if above or below:
			a = (sensor.x - dist) + abs(Y - sensor.y)
			b = (sensor.x + dist) - abs(Y - sensor.y)
			not_beacons.add((a, b))

	not_beacons = sorted(not_beacons)
	overlapping = [list(not_beacons[0])]
	for rng in not_beacons:
		rng = list(rng)
		prev = overlapping[-1]
		if rng[0] <= prev[1]:
			prev[1] = max(prev[1], rng[1])
		else:
			overlapping.append(rng)
	if len(overlapping) > 1:
		break

print((overlapping[0][1]+1) * 4000000 + Y)
