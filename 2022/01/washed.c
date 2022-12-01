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

void rot(long int top[3], long int sum)
{
	if (sum > top[0]) {
		top[2] = top[1];
		top[1] = top[0];
		top[0] = sum;
	}
	else if (sum > top[1]) {
		top[2] = top[1];
		top[1] = sum;
	}
	else if (sum > top[2])
		top[2] = sum;
}

int main()
{
	long int top[3];
	long int n, sum = 0;
	bool cont = true;
	while (cont) {
		switch (n = getn()) {
		case LONG_MIN+1:
			cont = false;
			break;
		case LONG_MIN:
			rot(top, sum);
			sum = 0;
			break;
		default:
			sum += n;
		}
	}
	printf("%ld\n", top[0]);
	printf("%ld\n", top[0] + top[1] + top[2]);
}
