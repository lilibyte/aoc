/*
  thank you No.84550907
  >If you're comparing the sums of indexes 0, 1, 2 and 1, 2, 3, then all you
  are really comparing is if index 3 is greater than index 0.
*/

#include <stdio.h>
#define SIZE 2000

int main() {
  int depths[SIZE];
  int part1 = 0, last = 0;
  for (int i = 0; i < SIZE; ++i) {
    scanf("%d", &depths[i]);
    if (i && depths[i] > last) {
      ++part1;
    }
    last = depths[i];
  }
  printf("%d\n", part1);

  int part2 = 0;
  for (int i = 0; i < SIZE-3; ++i) {
    if (depths[i+3] > depths[i]) {
      ++part2;
    }
  }
  printf("%d\n", part2);
}
