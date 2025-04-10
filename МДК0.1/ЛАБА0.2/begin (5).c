// Дано число A. Вычислить A^8, используя вспомогательную переменную 
//и три операции умножения. 
//Для этого последовательно находить A^2,A^4, A^8 Вывести все найденные степени числа A.*/
#include <stdio.h>
 int main()
{
    int a;
    printf("a:");
    scanf ("%d", &a);
    int stepa;
    stepa = a*a;
    printf("a^2:%d\n",stepa);
    stepa =stepa*stepa;
    printf("a^4:%d\n",stepa);
    stepa=stepa*stepa;
    printf("a^8:%d\n",stepa);
 
    return 0;
}