#include <stdio.h>

int cols[8][26];
char silver[9];
char gold[9];

int main()
{
	int end = 0;
	while (end != EOF) {
		for (int i = 0; i < 8; ++i)
			++cols[i][getchar() - 'a'];
		end = getchar();
		end = getchar();
		if (end != EOF)
			ungetc(end, stdin);
	}

	for (int i = 0; i < 8; ++i) {
		int max = 0;
		int max_c = 0;
		int min = 100;
		int min_c = 0;
		for (int j = 0; j < 26; ++j) {
			if (cols[i][j] > max) {
				max = cols[i][j];
				max_c = j;
			}
			if (cols[i][j] < min) {
				min = cols[i][j];
				min_c = j;
			}
		}
		silver[i] = max_c + 'a';
		gold[i] = min_c + 'a';
	}
	printf("%s\n", silver);
	printf("%s\n", gold);
}
