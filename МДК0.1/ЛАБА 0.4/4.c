//Задание 4. 
//Степень двойки. По данном числу N определить, является ли оно степенью числа 2.
//Входные данные: Одно целое неотрицательное число N.
//Выходные данные: YES - если число N является степенью двойки, и NO в противном случае.
#include <stdio.h>


int main()
{
    int N,i;
    i = 1;

    printf("N: ");
    scanf("%d", &N);

    while(i < N)
    {
        i = i * 2;
    }

    if (i == N || N == 1)
        printf("YES");
        
    else
        printf("NO");

    return 0;
}