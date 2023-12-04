#include <stdio.h>

/* #define wsz 5 */
/* #define nsz 8 */
/* #define cards 6 */
#define wsz 10
#define nsz 25
#define cards 205

int totals[cards];
int copies[cards];

int card()
{
	int c, points = 0, total = 0;
	static int sack = 0;
	int winning[wsz] = { 0 };
	while ((c = getchar()) != ':');
	getchar();
	for (int i = 0; i < wsz; ++i) {
		int a = getchar();
		int b = getchar();
		getchar();
		int n = 0;
		if (a != ' ')
			n = (a - '0') * 10;
		n += b - '0';
		winning[i] = n;
	}
	getchar(), getchar();
	for (int i = 0; i < nsz; ++i) {
		int a = getchar();
		int b = getchar();
		getchar();
		int n = 0;
		if (a != ' ')
			n = (a - '0') * 10;
		n += b - '0';
		for (int j = 0; j < wsz; ++j) {
			if (winning[j] == n) {
				points = points ? points * 2 : points + 1;
				++total;
			}
		}
	}
	totals[sack++] = total;
	return points;
}

void make_copy(int sack)
{
	copies[sack] += 1;
	for (int i = sack + 1; i < cards && i <= sack + totals[sack]; ++i)
		make_copy(i);
}

int main()
{
	int silver = 0, gold = 0;
	for (int i = 0; i < cards; ++i)
		silver += card();
	for (int i = 0; i < cards; ++i) {
		make_copy(i);
		gold += copies[i];
	}
	printf("%d\n", silver);
	printf("%d\n", gold);
}
