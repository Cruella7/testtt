/* Minmax6. Дано целое число N и набор из N целых чисел. Найти номера первого минимального и последнего максимального элемента 
из данного набора и вывести их в указанном порядке. */
/* Решение: Гусятинер Л.Б., для 22ИС-21, 27.01.2023 */

#include <stdio.h>
int main() {
    int n;
    scanf("%d", &n);
    int x, max;
    scanf("%d", &x);
    max = x;
    int imax1 = 0, imax2 = 0;
    int i = 1;
    while (i < n) {
        scanf("%d", &x);
        if (x > max) {
            max = x;
            imax1 = imax2 = i;
        }
        else if (x == max) {
            imax2 = i;
        }
        ++i;
    }
    printf("%d, %d\n", imax1, imax2);
    
    return 0;
}
/* Sample Input:
5
1 7 2 7 3
Sample OutPut:
1, 3
*/

