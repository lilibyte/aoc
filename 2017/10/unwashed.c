#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// this is the most poorly written AoC problem I can recall

int lengths[] = {225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110};

unsigned char lengths2[] = "225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"
                           "\x11\x1f\x49\x2f\x17";

#define LEN 256
#define LENLEN 16
#define HASHLEN 32

unsigned char elements[LEN];

int pos;
int skip;

void init()
{
	for (int i = 0; i < 256; ++i)
		elements[i] = i;
	pos = skip = 0;
}

void reverse(int pos, int n)
{
	int begin = 0;
	int end = n - 1;
	while (begin < end) {
		int b = (pos + begin) % LEN;
		int e = (pos + end) % LEN;
		int tmp = elements[b];
		elements[b] = elements[e];
		elements[e] = tmp;
		++begin;
		--end;
	}
}

void knot(int len)
{
	reverse(pos, len);
	pos = (pos + len + skip) % LEN;
	++skip;
}

int tie()
{
	init();
	for (int i = 0; i < LENLEN; ++i)
		knot(lengths[i]);
	return elements[0] * elements[1];
}

char *tie2()
{
	init();
	unsigned char dense[17] = { 0 };
	char *hash = malloc(HASHLEN + 1);
	for (int round = 0; round < 64; ++round)
		for (int i = 0; i < sizeof(lengths2) - 1; ++i)
			knot(lengths2[i]);
	for (int block = 0; block < 16; ++block) {
		int n = 0;
		for (int num = 0; num < 16; ++num)
			n ^= elements[16 * block + num];
		dense[block] = n;
	}
	for (int i = 0; i < 16; ++i)
		sprintf(hash + (i * 2), "%02x", dense[i]);
	return hash;
}


int main()
{
	int silver = tie();
	char *gold = tie2();
	printf("%d\n", silver);
	printf("%s\n", gold);
}
