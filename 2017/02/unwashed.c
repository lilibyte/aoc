#include <stdio.h>
#include <ctype.h>
#include <limits.h>
#include <stdbool.h>

void skip()
{
	int ch;
	while (isspace(ch = getchar()));
	ungetc(ch, stdin);
}

int sheet[16][16];

int main(int argc, char **argv)
{
	int ch, n = 0;
	int min = INT_MAX, max = 0;
	int y = 0, x = 0;
	int silver = 0, gold = 0;
	while (true) {
		while (isdigit(ch = getchar()))
			n = n * 10 + (ch - '0');
		if (n < min)
			min = n;
		if (n > max)
			max = n;
		sheet[y][x++] = n;
		n = 0;
		if (ch == '\n') {
			silver += max - min;
			min = INT_MAX;
			max = 0;
			x = 0;
			++y;
		}
		else if (ch == EOF)
			break;
		skip();
	}
	for (y = 0; y < 16; ++y) {
		for (x = 0; x < 16; ++x) {
			for (int i = 0; i < 16; ++i) {
				if (i == x)
					continue;
				if (sheet[y][x] % sheet[y][i] == 0)
					gold += sheet[y][x] / sheet[y][i];
			}
		}
	}
	printf("%d\n", silver);
	printf("%d\n", gold);
}
