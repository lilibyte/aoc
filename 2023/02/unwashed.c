#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>

int getn(int *n)
{
	int c, r = 0;
	while (!isdigit(c = getchar()) && c != EOF && c != '\n');
	if (c == EOF || c == '\n')
		return c;
	ungetc(c, stdin);
	while (isdigit(c = getchar()))
		r = r * 10 + c - '0';
	*n = r;
	return c;
}

int main()
{
	int i = 1, c = 0;
	int silver = 0, gold = 0;
	bool ok = true;
	while (c != EOF) {
		ok = true;
		while ((c = getchar()) != ':');
		getchar();
		int r = 0, g = 0, b = 0;
		int mr = 0, mg = 0, mb = 0;
		while (c != '\n') {
			int n;
			c = getn(&n);
			if (c == '\n' || c == EOF)
				break;
			int color = getchar();
			if (color == 'r')
				r += n;
			else if (color == 'g')
				g += n;
			else if (color == 'b')
				b += n;
			mr = (r > mr) ? r : mr;
			mg = (g > mg) ? g : mg;
			mb = (b > mb) ? b : mb;
			while ((c = getchar()) != ';' && c != ',' && c != '\n');
			if (c == ';' || c == '\n') {
				if (r > 12 || g > 13 || b > 14)
					ok = false;
				r = g = b = 0;
			}
		}
		printf("MAXES: %d,%d,%d\n", mr,mg,mb);
		gold += mr * mg * mb;
		if (ok)
			silver += i;
		if (i++ == 100)
			break;
	}
	printf("%d\n", silver);
	printf("%d\n", gold);
}
