/* Boolean8. Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел A и B нечетное». */
/* Гусятинер Л.Б., 27.01.2023. 4 минуты */
#include <stdio.h>
int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    int otvet = a % 2 != 0 && b % 2 != 0;
    printf("%d\n", otvet);
    /* Если не помните && || ! */
    if (a % 2 != 0) {
        if (b % 2 != 0)
            otvet = 1;
        else
            otvet = 0;
    }
    else
        otvet = 0;
    printf("%d\n", otvet);
    
    return 0;
}