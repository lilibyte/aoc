#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

long int getn()
{
	long int c, r = LONG_MIN, n = 0;
	while ((c = getchar()) >= '0' && c <= '9')
		r = n = n * 10 + c - '0';
	return c == EOF ? LONG_MIN+1 : r;
}

void rot(long int top[3], long int tmp)
{
	if (tmp > top[0]) {
		top[2] = top[1];
		top[1] = top[0];
		top[0] = tmp;
	}
	else if (tmp > top[1]) {
		top[2] = top[1];
		top[1] = tmp;
	}
	else if (tmp > top[2])
		top[2] = tmp;
}

int main()
{
	long int top[3];
	long int n, tmp = 0;
	bool cont = true;
	while (cont) {
		switch (n = getn()) {
		case LONG_MIN+1:
			cont = false;
			break;
		case LONG_MIN:
			rot(top, tmp);
			tmp = 0;
			break;
		default:
			tmp += n;
		}
	}
	printf("%ld\n", top[0]);
	printf("%ld\n", top[0] + top[1] + top[2]);
}
