#include <stdio.h>

// inspired by anon No.90072125 directly

int scores[3][3] = {
	4, 1, 7,
	8, 5, 2,
	3, 9, 6,
};

int scores2[3][3] = {
	3, 1, 2,
	4, 5, 6,
	8, 9, 7,
};

int main()
{
	int a, b, s = 0;
	int p1 = 0, p2 = 0;
	while (s != EOF) {
		a = getchar(), getchar(), b = getchar(), s = getchar();
		p1 += scores[b - 'X'][a - 'A'];
		p2 += scores2[b - 'X'][a - 'A'];
	}
	printf("%d\n%d\n", p1, p2);
}
