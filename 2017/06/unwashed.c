#include <stdio.h>
#include <ctype.h>
#include <stdint.h>

#define banks 16
int membank[banks];

#define buckets 9377
struct block {
	uint64_t hash;
	uint64_t cycle;
};
struct block hashtbl[buckets];

/* assumes `banks` <= 16 and each block in range 0b0000..0b1111 */
/* this worked until I realized a block can be > 15 */
/* uint64_t hashset(void) */
/* { */
/* 	uint64_t result = 0; */
/* 	for (int i = 0; i < banks; ++i) */
/* 		result |= (membank[i] << ((i % banks) * 4)); */
/* 	return result; */
/* } */

// based on https://stackoverflow.com/a/72073933
uint64_t hashset(void)
{
	uint64_t result = banks;
	for (int i = 0; i < banks; ++i) {
		unsigned x = membank[i];
		x = ((x >> 16) ^ x) * 0x45d9f3b;
		x = ((x >> 16) ^ x) * 0x45d9f3b;
		x = (x >> 16) ^ x;
		result ^= x + 0x9e3779b9 + (result << 6) + (result >> 2);
	}
	return result;
}

uint64_t cycle(void)
{
	int highest = 0, n = membank[0];  // init as first index in case it's highest
	for (int i = 0; i < banks; ++i)
		if (membank[i] > membank[highest])
			n = membank[highest = i];
	membank[highest++] = 0;  // inc highest before redistribution
	while (n--) {
		if (highest == banks)
			highest = 0;
		membank[highest++]++;
	}
	return hashset();
}

int getn(int *n)
{
	int c, r = 0;
	while (isspace((c = getchar())));
	ungetc(c, stdin);
	while (isdigit(c = getchar()))
		r = r * 10 + c - '0';
	*n = r;
	return c;
}

int main(int argc, char **argv)
{
	int silver = 0, gold = 0;
	int n, c, i = 0;
	while ((c = getn(&n)) != EOF)
		membank[i++] = n;
	while (1) {
		++silver;
		uint64_t hash = cycle();
		if (hashtbl[hash % buckets].hash && hashtbl[hash % buckets].hash == hash) {
			gold = silver - hashtbl[hash % buckets].cycle;
			break;
		}
		// does not handle collisions at all lol
		hashtbl[hash % buckets].hash = hash;
		hashtbl[hash % buckets].cycle = silver;
	}
	printf("%d\n", silver);
	printf("%d\n", gold);
}
