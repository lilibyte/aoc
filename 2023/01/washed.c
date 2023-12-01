#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define unset 999

char buf[256];
char *digits[10] = {
	"invalid", "one", "two", "three", "four",
	"five", "six", "seven", "eight", "nine"
};

void finddigits(int *f, int *fidx, int *l, int *lidx)
{
	char *first = NULL, *last = NULL;
	char *needle, *prev = buf;
	*f = *l = unset;
	for (int i = 1; i <= 9; ++i) {
		prev = buf;
		while ((needle = strstr(prev, digits[i]))) {
			if (!last || needle > last) {
				prev = needle + strlen(digits[i]) - 1;
				last = needle;
				*l = i;
				*lidx = last - buf;
			} else {
				++prev;
			}
			if (!first || needle < first) {
				first = needle;
				*f = i;
				*fidx = first - buf;
			}
		}
	}
}

int main()
{
	int silver = 0, gold = 0;
	char *c;
	while ((c = fgets(buf, 256, stdin))) {
		int first = unset, last;
		int first2, last2, fidx, lidx;
		finddigits(&first2, &fidx, &last2, &lidx);
		while (*c != '\n') {
			if (isdigit(*c)) {
				if (first == unset)
					last = first = *c - '0';
				if (first2 == unset || c - buf < fidx) {
					first2 = *c - '0';
					fidx = c - buf;
				}
				if (last2 == unset || c - buf > lidx) {
					last2 = *c - '0';
					lidx = c - buf;
				}
				break;
			}
			++c;
		}
		while (*c != '\n') {
			if (isdigit(*c)) {
				last = *c - '0';
				if (last2 == unset || c - buf > lidx) {
					last2 = *c - '0';
					lidx = c - buf;
				}
			}
			++c;
		}
		silver += first * 10 + last;
		gold += first2 * 10 + last2;
	}
	printf("%d\n", silver);
	printf("%d\n", gold);
}
