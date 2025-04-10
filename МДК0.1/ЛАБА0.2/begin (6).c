//Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти
//его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c).*/
#include <stdio.h>
 
int main()
{
    int a;
    printf("число a:");
    scanf ("%d", &a);
    int b;
    printf("число b:");
    scanf ("%d", &b);
    int c;
    printf("число c:");
    scanf ("%d", &c);
    int v= a*b*c;
    printf("v:%d\n",v);
    int s= (a*b+b*c+a*c)*2;
    printf("s:%d\n",s);
 
    return 0;
}