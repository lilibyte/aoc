#include <stdio.h>
#define W 40

long int reg = 1, cy = 1, silver;

long int addx()
{
	long int sign = 1, c, n = 0;
	getchar(), getchar(), getchar(), getchar(), c = getchar();
	if (c == '-') {
		sign = -1;
		c = getchar();
	}
	while (c >= '0' && c <= '9') {
		n = n * 10 + c - '0';
		c = getchar();
	}
	reg += n * sign;
	return c;
}

void draw()
{
	unsigned long int c = (cy-1) % W;
	putchar((c >= reg-1 && c <= reg+1) ? '#' : ' ');
	if (c == W-1)
		putchar('\n');
}

void cycle()
{
	if ((++cy) % W == 20)
		silver += cy * reg;
}

int main()
{
	char c = 0;
	while ((c = getchar()) != EOF) {
		draw();
		cycle();
		if (c == 'a') {
			draw();
			c = addx();
			cycle();
		}
		while (c != '\n') c = getchar();
	}
	printf("silver: %ld\n", silver);
}
