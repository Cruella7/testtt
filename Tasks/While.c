#include <stdio.h>

int main() {
    int N, count = 0, sum = 0;

    printf("Введите целое число N: ");
    if (scanf("%d", &N) != 1 || N <= 0) {
        printf("Введите положительное число.\n");
        return 1;
    }

    while (N > 0) {
        int digit = N % 10;
        count++;
        sum += digit;
        N /= 10;
    }

    printf("Количество цифр: %d\n", count);
    printf("Сумма цифр: %d\n", sum);

    return 0;
}
