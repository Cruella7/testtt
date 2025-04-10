/** М. Э. Абрамян. 1000 ЗАДАЧ ПО ПРОГРАММИРОВАНИЮ, Ростов-на-Дону 2004.
Решение: Гусятинер Л.Б., 22.09.2020

Param1. Описать функцию MinElem(A, N) целого типа, находящую минимальный элемент
целочисленного массива A размера N. С помощью этой функции найти минимальные элементы
массивов A, B, C размера NA, NB, NC соответственно.
*/

#include <stdio.h>

int minElem(int *a, size_t n);
int main()
{
    int v[] = {331,3,5,2,6};
    size_t n = sizeof(v) / sizeof(int);
    printf("%d\n", minElem(v, n));
    getchar();

    return 0;
}

int minElem(int *a, size_t n)
{
    int min = a[0];
    size_t i;
    for (i = 1; i < n; ++i)
        if (a[i] < min)
            min = a[i];
    return min;
}
