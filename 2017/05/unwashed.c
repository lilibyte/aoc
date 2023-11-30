#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int tapelen;
int tape[2048];
int tape2[2048];

int seek2(void)
{
	static int cur = 0;
	if (cur >= tapelen)
		return 0;
	cur += tape2[cur] >= 3 ? tape2[cur]-- : tape2[cur]++;
	return 1;
}

int seek(void)
{
	static int cur = 0;
	if (cur >= tapelen)
		return 0;
	cur += tape[cur]++;
	return 1;
}

int getn(int *n)
{
	int c = getchar(), sign = -1, r = 0;
	if (c != '-') {
		sign = 1;
		ungetc(c, stdin);
	}
	while (isdigit(c = getchar()))
		r = r * 10 + c - '0';
	*n = r * sign;
	return c;
}

int main(int argc, char **argv)
{
	int n = 0;
	while (getn(&n) != EOF)
		tape2[tapelen] = tape[tapelen] = n, ++tapelen;

	int silver = 0, gold = 0;
	while (seek())
		++silver;
	while (seek2())
		++gold;

	printf("%d\n", silver);
	printf("%d\n", gold);
}
