//Даны катеты прямоугольного треугольника a и b. Найти его гипотенузу c и периметр P

#include <stdio.h>
int main()
{   
    printf(" Введиет первый катет ");
    float a;
    scanf("%f", &a);
    printf(" Введите второй катет ");
    float b;
    scanf("%f", &b);
    float c = sqrt((a*a) + (b*b));
    float p = a + b + c;
    printf("гипотенуза = %.2f",c );
    printf("периметр = %.2f\n", p);
    return 0;
}