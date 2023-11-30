/* NOTE: does not check for hash collision */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* #include "aoc.h" */

// ---- stuff from my incomplete aoc.h ----

#define find(str, sub) (strstr((str), (sub)))

#define bufsz 1024
char buf[bufsz];

char *input(char *filename)
{
	static FILE *file = NULL;
	char *line = NULL;
	if (file == NULL && (filename == NULL || *filename == '\0'))
		file = stdin;
	else if (file == NULL) {
		file = fopen(filename, "r");
		if (file == NULL)
			return NULL;
	}
	line = fgets(buf, 1024, file);
	if (line == NULL)
		return NULL;
	buf[strcspn(buf, "\n")] = '\0';
	line = malloc(strlen(buf) + 1);
	if (line == NULL)
		return NULL;
	return strcpy(line, buf);
}

char **split(char *str, char *sep)
{
	if (str == NULL)
		return NULL;

	int listsz = 8;
	int listlen = 0;
	int seplen = sep ? strlen(sep) : 0;

	if (sep == NULL || *sep == '\0')
		listsz = strlen(str) + 1;

	char **list = malloc(sizeof(char *) * listsz);
	if (list == NULL)
		return NULL;

	char *iter = NULL;
	char *new = NULL;

	if (sep == NULL || *sep == '\0') {
		for (int i = 0; i < listsz - 1; ++i) {
			new = malloc(2);
			if (new == NULL)
				return NULL;
			new[0] = str[i];
			new[1] = '\0';
			list[i] = new;
		}
		list[listsz - 1] = NULL;
		return list;
	}

	for (int i = 0; i < listsz; ++i)
		list[i] = NULL;

	while ((iter = find(str, sep))) {
		new = malloc(iter - str + 1);
		if (new == NULL)
			return NULL;
		strncpy(new, str, iter - str);
		new[iter - str] = '\0';
		str = iter + seplen;
		list[listlen++] = new;
		if (listlen == listsz - 1) {
			listsz *= 4;
			list = realloc(list, sizeof(char *) * listsz);
			if (list == NULL)
				return NULL;
			for (int i = listlen; i < listsz; ++i)
				list[i] = NULL;
		}
	}

	// ???
	if (listlen) {
		new = malloc(strlen(str) + 1);
		if (new == NULL)
			return NULL;
		strcpy(new, str);
		if (listlen == listsz - 1) {
			listsz *= 4;
			list = realloc(list, sizeof(char *) * listsz);
			if (list == NULL)
				return NULL;
			for (int i = listlen; i < listsz; ++i)
				list[i] = NULL;
		}
		list[listlen++] = new;
	}

	return list;
}

void freelist(char **list)
{
	char **iter = list;
	while (*iter)
		free(*iter++);
	free(list);
}

// ----   solution starts below here   ----

#define hashsz 991

unsigned djb2(char *s)
{
	unsigned c, hash = 5381;
	while ((c = *s++))
		hash = (hash << 5) + 5 + c;
	return hash;
}

int chcmp(const void *a, const void *b)
{
	return *(char *)a - *(char *)b;
}

void sortwords(char **words)
{
	while (*words) {
		qsort(*words, strlen(*words), 1, chcmp);
		++words;
	}
}

int isvalid(char **words)
{
	static unsigned table[hashsz];
	for (int i = 0; i < hashsz; table[i++] = 0);
	while (*words) {
		unsigned hash = djb2(*words);
		unsigned bucket = hash % hashsz;
		if (table[bucket] == hash)
			return 0;
		table[bucket] = hash;
		++words;
	}
	return 1;
}

int main(int argc, char **argv)
{
	int silver = 0, gold = 0;
	char *line = NULL;
	while ((line = input("input04"))) {
		char **words = split(line, " ");
		silver += isvalid(words);
		sortwords(words);
		gold += isvalid(words);
		free(line);
		/* free(words); */
		freelist(words);
	}
	printf("%d\n", silver);
	printf("%d\n", gold);
}
