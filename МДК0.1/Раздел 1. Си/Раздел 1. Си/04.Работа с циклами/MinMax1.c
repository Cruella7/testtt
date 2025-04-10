/// М. Э. Абрамян. 1000 ЗАДАЧ ПО ПРОГРАММИРОВАНИЮ, Ростов-на-Дону 2004.
/// Minmax1. Дано целое число N и набор из N чисел. Найти минимальный и
/// максимальный из элементов данного набора и вывести их в указанном порядке.
/// Решение: Гусятинер Л.Б., 05.09.2020

#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int min, max;
    int x;
    scanf("%d", &x);
    min = max = x;
    for (int i = 1; i < n; ++i) {
        scanf("%d", &x);
        if (x < min)
            min = x;
        else if (x > max)
            max = x;
    }
    printf("%d %d\n", min, max);

    getchar();
    return 0;
}
