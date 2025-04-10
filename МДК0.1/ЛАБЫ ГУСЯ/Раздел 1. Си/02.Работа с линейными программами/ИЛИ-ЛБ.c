/* Пример отличия логического и побитового ИЛИ.
Гусятинер Л.Б. КМПО РАНХиГС, 29.01.2023 */

#include <stdio.h>
int main()
{
    int a = 5,b = 7;
    int c = a | b;
    int d = a || b;
    printf("a | b = %d\n", c); // 7
    printf("a || b = %d\n", d); // 1
    return 0;
}
