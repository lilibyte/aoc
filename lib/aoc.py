from fileinput import input
from more_itertools import consume
from toolz import pipe, isiterable
import re

def iseven(i):
	return i % 2 == 0

def isodd(i):
	return i % 2 == 1

def ipipe(it, *funcs):
	"Pass iterator to toolz.pipe() and yield its result"
	if not isiterable(it):
		it = [it]
	for i in it:
		yield pipe(i, *funcs)

def cpipe(it, *funcs):
	"Pass iterator to toolz.pipe() and discard its result"
	if not isiterable(it):
		it = [it]
	for i in it:
		pipe(i, *funcs)

def cmap(func, data):
	"Consume map object and discard its evaluated form"
	consume(map(func, data))

def static(**kwargs):
	def decorate(func):
		for k in kwargs:
			setattr(func, k, kwargs[k])
		return func
	return decorate

def atoi(s: str, base: int = None):
	if isinstance(s, int):
		return s
	elif base:
		return int(s, base)
	elif s.isdigit():
		return int(s)
	else:
		return s

def scan(re_str: str):
	r = re.compile(re_str)
	for line in input():
		for m in re.finditer(r, line):
			if len(m.groups()) == 1:
				yield atoi(m.group(1))
			elif len(m.groups()) > 1:
				yield tuple(atoi(t) for t in m.groups())
			else:
				yield line.strip()
