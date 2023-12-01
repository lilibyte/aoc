#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define unset 999

char buf[256];
char *digits[10] = {
	"ERROR", "one", "two", "three", "four",
	"five", "six", "seven", "eight", "nine"
};

void finddigits(int *f, int *fidx, int *l, int *lidx)
{
	int i;
	char *first = NULL, *last = NULL;
	char *prev = buf;
	char *needle;
	*f = unset;
	*l = unset;
	for (i = 1; i <= 9; ++i) {
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
	int first, last;
	/* while (c != EOF) { */
	/* 	first = last = unset; */
	/* 	while ((c = getchar()) != '\n' && c != EOF) { */
	/* 		if (isdigit(c)) { */
	/* 			last = first = c; */
	/* 			break; */
	/* 		} */
	/* 	} */
	/* 	if (c != '\n' && c != EOF) { */
	/* 		while ((c = getchar()) != '\n' && c != EOF) { */
	/* 			if (isdigit(c)) */
	/* 				last = c; */
	/* 		} */
	/* 	} */
	/* 	if (c != EOF && first != unset) { */
			/* printf("%d\n", (first - '0') * 10 + last - '0'); */
			/* printf("%d %d\n", first - '0', last - '0'); */
	/* 		silver += (first - '0') * 10 + last - '0'; */
	/* 	} */
	/* } */
	/* printf("%d\n", silver); */
	char *c;
	while (fgets(buf, 256, stdin)) {
		c = buf;
		int fidx, lidx;
		bool ffuck = false;
		bool lfuck = false;
		finddigits(&first, &fidx, &last, &lidx);
		while (*c != '\n') {
			if (isdigit(*c)) {
				if (first == unset || c - buf < fidx) {
					first = *c - '0';
					fidx = c - buf;
					ffuck = true;
				}
				if (last == unset || c - buf > lidx) {
					last = *c - '0';
					lidx = c - buf;
					lfuck = true;
				}
				break;
			}
			++c;
		}
		while (*c != '\n') {
			if (isdigit(*c)) {
				if (last == unset || c - buf > lidx) {
					last = *c - '0';
					lidx = c - buf;
					lfuck = true;
				}
			}
			++c;
		}
		silver += first * 10 + last;
		buf[strcspn(buf,"\n")] = 0;
		if (fidx)
			printf("%.*s", fidx, buf);
		if (!ffuck)
			printf("\e[1m%.*s\e[0m", (int)strlen(digits[first]), buf + fidx);
		else
			printf("\e[1m%d\e[0m", *(buf + fidx) - '0');
		if (fidx == lidx)
			printf("%s", buf + fidx + 1);
		else {
			if (!ffuck)
				printf("%.*s", lidx - (fidx + (int)strlen(digits[first])),
						buf + fidx + (int)strlen(digits[first]));
			else
				printf("%.*s", lidx - fidx - 1, buf + fidx + 1);
		}
		// -----
		if (fidx != lidx) {
		if (!lfuck)
			printf("\e[1m%.*s\e[0m", (int)strlen(digits[last]), buf + lidx);
		else
			printf("\e[1m%d\e[0m", *(buf + lidx) - '0');
		if (!lfuck)
			printf("%s",  buf + lidx + strlen(digits[last]));
		else
			printf("%s",  buf + lidx + 1);
		}
		printf("%*d\n", 60 - (int)strlen(buf), first * 10 + last);
	}
	printf("%d\n", silver);
}
