/** М. Э. Абрамян. 1000 ЗАДАЧ ПО ПРОГРАММИРОВАНИЮ, Ростов-на-Дону 2004.
Matrix1. Даны целые положительные числа M и N. Сформировать целочисленную
матрицу размера M * N, у которой все элементы i-й строки имеют значение
10*i (i = 1, …, m).
Решение Гусятинер Л.Б., 10.2012 */

#include <stdio.h>
const size_t MAXM = 10;
const size_t MAXN = 10;

int main() {
    int i, j;
    int a[MAXM][MAXN];
    int m, n;

    scanf("%d%d", &m, &n);
    for (i = 0; i < m; ++i) {
        for (j = 0; j < n; ++j) {
            a[i][j] = 10 * i;
        }
    }

    for (i = 0; i < m; ++i) {
        for (j = 0; j < n; ++j)
            printf("%4d", a[i][j]);
        printf("\n");
    }
    getchar();
    return 0;
}
