from fileinput import input
from collections import defaultdict as ddict
from itertools import tee
from toolz import get
from aoc import static, cpipe

keys = {"^": 1, "v": -1, ">": 1, "<": -1}
mv1, mv2 = tee(iter(next(input())))
dd = ddict(int)
dd[0,0] = 1

def deliver(xy):
	dd[xy] += 1

def getdir(dirmap):
	return sum(get(["^","v"], dirmap)), sum(get(["<",">"], dirmap))

@static(ds=ddict(int))
def getloc(d):
	getloc.ds[d] += keys[d]
	return getdir(getloc.ds)

@static(ds=ddict(int), ds2=ddict(int), turn=1)
def getloc2(d):
	getloc2.turn = not getloc2.turn
	if getloc2.turn:
		getloc2.ds2[d] += keys[d]
		return getdir(getloc2.ds2)
	else:
		getloc2.ds[d] += keys[d]
		return getdir(getloc2.ds)

cpipe(mv1, getloc, deliver)
print(len(dd))

dd = ddict(int)
dd[0,0] = 1

cpipe(mv2, getloc2, deliver)
print(len(dd))
