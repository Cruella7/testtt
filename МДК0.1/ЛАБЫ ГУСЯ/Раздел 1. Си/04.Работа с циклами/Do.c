/* Вводится целое неотрицательное число. Перевернуть */
/* Цикл do .. while */
#include <stdio.h>

int main()
{
    int num;
    int reversed = 0;
    scanf("%d", &num);
    do {
        reversed = reversed * 10 + num % 10;
        num /= 10;
    } while (num > 0);
    printf("%d\n", reversed);

    return 0;
}
