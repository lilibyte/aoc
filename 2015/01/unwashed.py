from fileinput import input

# part 1
i = next(input())
print(i.count("(") - i.count(")"))

# part 2
f = 0
for p, c in enumerate(i, start=1):
	match c:
		case "(":
			f += 1
		case ")":
			f -= 1
	if f == -1:
		print(p)
		break
