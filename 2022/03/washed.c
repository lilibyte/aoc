#include <stdio.h>
#include <stdint.h>

#define MAX 48

int main()
{
	long int silver = 0, gold = 0;
	uint64_t a = 0, b = 0;
	int len = 0, x = 1, c;
	char line[MAX];
	uint64_t last[3];
	while (1) {
		while ((c = getchar()) > 'A')
			line[len++] = (c - ((c >= 'a') ? ('a') : ('A' - 26)));
		if (c == EOF)
			break;
		for (int i = 0; i < len/2; ++i) {
			a |= (1UL << line[i]);
			b |= (1UL << line[(len-1)-i]);
		}
		silver += __builtin_ctzl(a & b) + 1;
		last[x % 3] = a | b;
		if (x++ % 3 == 0)
			gold += __builtin_ctzl(last[0] & last[1] & last[2]) + 1;
		a = b = len = 0;
	}
	printf("%ld\n", silver);
	printf("%ld\n", gold);
}
