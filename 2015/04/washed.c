#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "aoc.h"

#define INPUT "ckczppom"
#define INPUT_SZ sizeof(INPUT)

bool validhash_p1(byte *md) {
	return !md[0] && !md[1] && !(md[2] >> 4);
}

bool validhash_p2(byte *md) {
	return !md[0] && !md[1] && !md[2];
}

i64 n;

bool validhash(byte *md) {
	static bool p1 = false;
	if (p1)
		return validhash_p2(md);
	if ((p1 = validhash_p1(md)))
		printf("part 1: %ld\n", n);
	return false;
}

int main() {
	str s = malloc(32);
	str a = malloc(32);
	byte *md = malloc(16);
	memcpy(s, INPUT, INPUT_SZ);

	do {
		sz i = itoa(++n, a, 10);
		memcpy(s+8, a, i+1);
		md5(s, INPUT_SZ-1 + i, md);
	} while (!validhash(md));

	printf("part 2: %ld\n", n);
}
