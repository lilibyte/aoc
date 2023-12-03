#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 142

char schematic[MAX][MAX];
struct gear { int len; int ratio; };
struct gear gears[MAX][MAX];

void fill()
{
	int c, y = 0, x = 0;
	while ((c = getchar()) != EOF) {
		if (x == 0)
			schematic[y][x++] = '.';
		if (c == '\n') {
			++y;
			schematic[y][x] = '.';
			x = 0;
			continue;
		}
		schematic[y][x++] = c;
	}
}

bool issymbol(char c)
{
	return c != '.' && ispunct(c);
}

void gear_add(struct gear *gear, int n)
{
	if (gear->ratio == 0)
		gear->ratio = 1;
	gear->ratio *= n;
	gear->len += 1;
}

#define gear_check(g) if (s == '*') gear_add((g), atoi(&schematic[y][x]))

int ispart(int x, int y)
{
	int len = 0, s;
	while (x + len < MAX && isdigit(schematic[y][x+len]))
		++len;
	if (x + len < MAX) {
		// check if character to direct right is a symbol
		if (issymbol((s = schematic[y][x+len]))) {
			gear_check(&gears[y][x+len]);
			return atoi(&schematic[y][x]);
		}
		// check if character to bottom right is a symbol
		if (y < MAX - 1) {
			if (issymbol((s = schematic[y+1][x+len]))) {
				gear_check(&gears[y+1][x+len]);
				return atoi(&schematic[y][x]);
			}
		}
		// check if character to top right is a symbol
		if (y > 0) {
			if (issymbol((s = schematic[y-1][x+len]))) {
				gear_check(&gears[y-1][x+len]);
				return atoi(&schematic[y][x]);
			}
		}
	}
	if (x > 0) {
		// check if character to direct left is a symbol
		if (issymbol((s = schematic[y][x-1]))) {
			gear_check(&gears[y][x-1]);
			return atoi(&schematic[y][x]);
		}
		// check if character to bottom left is a symbol
		if (y < MAX - 1) {
			if (issymbol((s = schematic[y+1][x-1]))) {
				gear_check(&gears[y+1][x-1]);
				return atoi(&schematic[y][x]);
			}
		}
		// check if character to top left is a symbol
		if (y > 0) {
			if (issymbol((s = schematic[y-1][x-1]))) {
				gear_check(&gears[y-1][x-1]);
				return atoi(&schematic[y][x]);
			}
		}
	}
	// check if any characters to direct top are a symbol
	if (y > 0) {
		for (int i = 0; i < len; ++i) {
			if (issymbol((s = schematic[y-1][x+i]))) {
				gear_check(&gears[y-1][x+i]);
				return atoi(&schematic[y][x]);
			}
		}
	}
	// check if any characters to direct bottom are a symbol
	if (y < MAX - 1) {
		for (int i = 0; i < len; ++i) {
			if (issymbol((s = schematic[y+1][x+i]))) {
				gear_check(&gears[y+1][x+i]);
				return atoi(&schematic[y][x]);
			}
		}
	}
	return 0;
}

char *getnums(int *x, int *y)
{
	static int _x = 0, _y = 0;
	if (_y >= MAX)
		return NULL;
	while (!isdigit(schematic[_y][_x])) {
		if (++_x == MAX) {
			_x = 0;
			if (++_y == MAX)
				return NULL;
		}
	}
	*x = _x;
	*y = _y;
	while (_x < MAX && isdigit(schematic[_y][_x]))
		++_x;
	if (_x >= MAX) {
		_x = 0;
		++_y;
	}
	return &schematic[*y][*x];
}

int main()
{
	fill();
	int silver = 0, gold = 0;
	int x = 0, y = 0;
	while (getnums(&x, &y))
		silver += ispart(x, y);
	for (int y = 0; y < MAX; ++y)
		for (int x = 0; x < MAX; ++x)
			if (gears[y][x].len > 1)
				gold += gears[y][x].ratio;
	printf("%d\n", silver);
	printf("%d\n", gold);
}
