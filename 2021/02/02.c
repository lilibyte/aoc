#include <stdio.h>

int main() {
  int horiz = 0, depth = 0, depth2 = 0, all = 0, value = 0;
  char line[11];
  for (int i = 0; i < 1000; ++i) {
    fgets(line, 11, stdin);
    sscanf(line, "%*[^0123456789]%d", &value);
    switch (line[0]) {
      case 'f':
        horiz += value;
        depth2 += value * all;
        break;
      case 'd':
        depth += value;
        all += value;
        break;
      case 'u':
        depth -= value;
        all -= value;
        break;
    }
  }
  printf("%d\n", horiz * depth);
  printf("%d\n", horiz * depth2);
}
