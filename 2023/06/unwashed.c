#include <stdio.h>
#include <stdint.h>

uint64_t time[] = { 44, 82,  69, 81 };
uint64_t dist[] = { 202, 1076, 1138, 1458 };
uint64_t time2 = 44826981;
uint64_t dist2 = 202107611381458;

uint64_t race(uint64_t speed, uint64_t t, uint64_t d)
{
	uint64_t distance = speed * (t - speed);
	// I'm so bad at math I did this initally ;_;
	/* for (int i = 0; i < time[r] - speed; ++i) */
	/* 	distance += speed; */
	return distance > d;
}

int main()
{
	uint64_t silver = 1, gold = 1;
	for (uint64_t r = 0; r < sizeof(time) / sizeof(uint64_t); ++r) {
		uint64_t total = 0;
		for (uint64_t i = 0; i <= time[r]; ++i)
			total += race(i, time[r], dist[r]);
		silver *= total;
	}
	uint64_t total = 0;
	for (uint64_t i = 0; i <= time2; ++i)
		total += race(i, time2, dist2);
	gold *= total;
	printf("%lu\n", silver);
	printf("%lu\n", gold);
}
