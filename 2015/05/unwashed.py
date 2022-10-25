from aoc import split
from string import ascii_lowercase
from placeholder import _
from toolz import juxt, compose
from fileinput import input
from itertools import pairwise, tee
from more_itertools import triplewise

p1, p2 = tee(input())

def has_n_vowels(s, n=3):
	return sum(map(s.count, split("aeiou"))) >= n

def has_repeated_letter(s):
	return any(map(s.count, map(_ * 2, split(ascii_lowercase))))

def substr_not_in(s, ss=("ab", "cd", "pq", "xy")):
	return not any(map(s.count, ss))

nice = compose(all, juxt(substr_not_in, has_repeated_letter, has_n_vowels))
print(sum(map(nice, p1)))

def has_pairs(s):
	return bool(sum(map(lambda x: s.count("".join(x)) > 1, pairwise(s))))

def has_surrounded_letter(s):
	return bool(sum(map(lambda x: x[0] == x[2], triplewise(s))))

nice2 = compose(all, juxt(has_pairs, has_surrounded_letter))
print(sum(map(nice2, p2)))
