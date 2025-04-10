/** For16. Дано вещественное число A и целое число N (> 0). Используя один цикл,
вывести все целые степени числа A от 1 до N. */
#include <stdio.h>
int main() {
    int n;
    scanf("%d", &n);
    double a;
    scanf("%lf", &a);
    double b = 1;
    int i = 1;
    while (i <= n) {
        b = b * a;
        printf("%.2f ", b);
        i = i + 1;
    }
    return 0;
}
