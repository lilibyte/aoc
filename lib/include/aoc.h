#ifndef AOC_H
#define AOC_H

#include <stdlib.h>
#include <stdint.h>

// https://stackoverflow.com/q/11761703/
#define GET_MACRO(_0, _1, _2, NAME, ...) NAME
#define md5(...) GET_MACRO(__VA_ARGS__, md53, md52, md51)(__VA_ARGS__)
#define md51(in) _md5_1(in)
#define md52(in, len) _md5_2(in, len)
#define md53(in, len, md) _md5_3(in, len, md)

#define hex(...) GET_MACRO(__VA_ARGS__, hex3, hex2, hex1)(__VA_ARGS__)
#define hex1(in) _hex_1(in)
#define hex2(in, len) _hex_3(in, len, NULL)
#define hex3(in, len, result) _hex_3(in, len, result)

typedef char * str;
typedef int8_t i8;
typedef int16_t i16;
typedef int32_t i32;
typedef int64_t i64;
typedef uint8_t byte;
typedef uint8_t u8;
typedef uint16_t u16;
typedef uint32_t u32;
typedef uint64_t u64;
typedef size_t sz;

str _hex_1(i64 i);
str _hex_2(const byte *bin, sz len);
str _hex_3(const byte *bin, sz len, str *result);

byte *_md5_1(str in);
byte *_md5_3(str in, sz len, byte *md);

size_t itoa(int value, char *result, int base);

#endif // AOC_H
