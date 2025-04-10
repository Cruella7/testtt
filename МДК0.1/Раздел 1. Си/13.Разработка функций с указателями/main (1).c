#include <stdio.h>
void DigitCountSum(int k, int *pc, int *ps) {
    int d = 0;
    *pc = *ps = 0;
    do {
        ++*pc;
        *ps += k % 10;
        k /= 10;
    } while (k);
}

int main() {
    int num = 12340;
    int c, s;
    DigitCountSum(num, &c, &s);
    printf("c=%d, s=%d\n", c, s);
    return 0;
}