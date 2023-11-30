#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>

#define altoi(c) ((c) - 'a')
#define itoal(i) ((i) + 'a')

struct reg {
	struct reg *next;
	int val;
};

struct reg registers[26];

enum op {
	NONE,
	GT,   LT,
	GTE, LTE,
	EQ,  NEQ
};

int getn(void)
{
	int c, r = 0, sign = 1;
	if ((c = getchar()) == '-')
		sign = -1;
	else
		ungetc(c, stdin);
	while (isdigit(c = getchar()))
		r = r * 10 + c - '0';
	return r * sign;
}

struct reg *getreg(void)
{
	int c = getchar(), c2, c3;
	if (c == EOF)
		return NULL;
	// ----------
	c2 = getchar();
	struct reg *r1 = registers + altoi(c);
	if (c2 == ' ')
		return r1;
	// ----------
	if (r1->next == NULL)
		r1->next = calloc(26, sizeof(struct reg));
	c3 = getchar();
	struct reg *r2 = r1->next + altoi(c2);
	if (c3 == ' ')
		return r2;
	// ----------
	if (r2->next == NULL)
		r2->next = calloc(26, sizeof(struct reg));
	struct reg *r3 = r2->next + altoi(c3);
	getchar(); // ' '
	return r3;
}

int getop(void)
{
	int c = getchar();
	int c2 = getchar();
	if (c2 != ' ')
		getchar();
	switch (c) {
	case '=':  return EQ;
	case '!':  return NEQ;
	case '>':  return (c2 == ' ') ? GT : GTE;
	case '<':  return (c2 == ' ') ? LT : LTE;
	default:   return NONE;
	}
}

bool test(int a, int b, enum op op)
{
	switch (op) {
	case   GT:  return a >  b;
	case  GTE:  return a >= b;
	case   LT:  return a <  b;
	case  LTE:  return a <= b;
	case   EQ:  return a == b;
	case  NEQ:  return a != b;
	default:    return false;
	}
}

int expr(int *gold)
{
	struct reg *reg = getreg();
	if (reg == NULL)
		return 0;
	int sign = (getchar() == 'i') ? 1 : -1;
	getchar(), getchar(), getchar();
	int by = getn();
	if (sign == -1)
		by = -by;
	getchar(), getchar(), getchar();
	struct reg *reg2 = getreg();
	int op = getop(), n = getn();
	if (test(reg2->val, n, op)) {
		reg->val += by;
		if (reg->val > *gold)
			*gold = reg->val;
	}
	return 1;
}

int findlargest(void)
{
	int find(struct reg *reg, int n)
	{
		int l = 0;
		for (int i = 0, r; i < 26; ++i) {
			if (reg[i].val > l)
				l = reg[i].val;
			if (reg[i].next && ((r = find(reg[i].next, l)) > l))
				l = r;
		}
		return l;
	}
	return find(registers, 0);
}

int main(int argc, char **argv)
{
	int gold = 0;
	while (expr(&gold));
	int silver = findlargest();
	printf("%d\n", silver);
	printf("%d\n", gold);
}
