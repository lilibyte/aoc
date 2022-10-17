from fileinput import input
import re

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
