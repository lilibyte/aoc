#include <stdlib.h>
#include <openssl/md5.h>
#include <string.h>
#include <stdio.h>

#include "aoc.h"

str _hex_1(i64 in) {
	str s = malloc(sizeof(i64)*2 + 1);
	sprintf(s, "%lx", in);
	return s;
}

str _hex_3(const byte *bin, sz binlen, str *result) {
	unsigned char hex_str[]= "0123456789abcdef";
	if (result == NULL)
		result = malloc(sizeof(unsigned char *));

	if (!(*result = malloc(binlen * 2 + 1)))
		return (NULL);

	(*result)[binlen * 2] = 0;

	if (!binlen)
		return (NULL);

	for (unsigned int i = 0; i < binlen; i++) {
		(*result)[i * 2 + 0] = hex_str[(bin[i] >> 4) & 0x0F];
		(*result)[i * 2 + 1] = hex_str[(bin[i]     ) & 0x0F];
	}
	return (*result);
}

byte *_md5_3(str in, sz len, byte *md) {
	MD5((u8*)in, len, md);
	return md;
}

byte *_md5_2(str in, sz len) {
	byte *md = malloc(16);
	MD5((u8*)in, len, md);
	return md;
}

byte *_md5_1(str in) {
	sz len = strlen((char*)in);
	byte *md = malloc(16);
	MD5((unsigned char*)in, len, md);
	return md;
}

/**
 * C++ version 0.4 char* style "itoa":
 * Written by Lukás Chmela
 * Released under GPLv3.
 * https://www.strudel.org.uk/itoa/
 *
 * Modified to return the length of the
 * digit string instead of the result.
 */
size_t itoa(int value, char* result, int base) {
    // check that the base if valid
    if (base < 2 || base > 36) { *result = '\0'; return 0; }

    char* ptr = result, *ptr1 = result, tmp_char;
    int tmp_value;
	size_t len = 0;

    do {
        tmp_value = value;
        value /= base;
        *ptr++ = "zyxwvutsrqponmlkjihgfedcba9876543210123456789abcdefghijklmnopqrstuvwxyz" [35 + (tmp_value - value * base)];
		++len;
    } while ( value );

    // Apply negative sign
    if (tmp_value < 0) *ptr++ = '-';
    *ptr-- = '\0';
    while(ptr1 < ptr) {
        tmp_char = *ptr;
        *ptr--= *ptr1;
        *ptr1++ = tmp_char;
    }
    return len;
}
