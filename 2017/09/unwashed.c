#include <stdio.h>
#include <stdbool.h>

bool follows_garbage;
bool isneighbor;
int depth;

int silver, gold;

int token(void)
{
	int ch;
	while (true) {
		switch ((ch = getchar())) {
		case ',':
		case '!':
		case '{':
		case '}':
		case '<':
		case '>':
			return ch;
		default:
			if (ch == '\n' || ch == EOF)
				return 0;
		}
	}
}

void discard(void)
{
	int ch;
	while (true) {
		ch = getchar();
		if (ch == '!')
			getchar();
		else if (ch == '>')
			return;
		else
			++gold;
	}
}

int parse(int tok)
{
	switch (tok) {
	case '{':
		if (!isneighbor)
			++depth;
		isneighbor = false;
		silver += depth;
		break;
	case '}':
		--depth;
		break;
	case '<':
		discard();
		if (isneighbor)
			--depth;
		isneighbor = false;
		follows_garbage = true;
		break;
	case ',':
		if (!follows_garbage)
			isneighbor = ++depth;
		follows_garbage = false;
		break;
	}
	return tok;
}

int main()
{
	while (parse(token()));
	printf("%d\n", silver);
	printf("%d\n", gold);
}
