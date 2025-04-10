//Дана сторона квадрата a. Найти его периметр P = 4·a.

#include <stdio.h>
int main ()
{
    float a;
    printf("a:");
    scanf("%f", &a);
    float P= 4*a;
    printf("P:%\n", P);
    return 0;
}