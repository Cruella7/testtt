/* Вводится N чисел. Найти сумму */
/* Цикл for, вынесли инкремент в тело */
#include <stdio.h>

int main()
{
    int i;
    int sum = 0;
    int n, x;
    scanf("%d", &n);
    for (i = 0; i < n; ) {
        scanf("%d", &x);
        sum += x;
        ++i;
    }
    printf("%d\n", sum);

    return 0;
}
