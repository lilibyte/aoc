from hashlib import md5

key = "ckczppom"

def hashgen(n):
	return md5((key+str(n)).encode("utf-8")).hexdigest()

def mine(zeros, n=1):
	while not hashgen(n).startswith("0" * zeros):
		n += 1
	return n

print(mine(5))
print(mine(6))
