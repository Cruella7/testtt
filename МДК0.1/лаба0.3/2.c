//Задание 2. Вычислить номер дня в невисокосном году по заданным числу и месяцу.
//Входные данные: Два целых числа. Первое число m - номер месяца. Второе число d -
//номер дня в месяце. Выходные данные: Одно целое число - порядковый номер дня в
//невисокосном году.

//22ИС-21, Арутюнян Софья Лабораторная работа 0.3 Работа с ветвлением и выбором.
#include <stdio.h>

int main() {
    int m, d, nv;
    scanf("%d %d", &m,&d);
    switch(m){
        case 1:nv=d;
        break;
        case 2:nv=31+d;
        break;
        case 3:nv=59+d;
        break;
        case 4:nv=90+d; 
        break;
        case 5:nv=120+d; 
        break;
        case 6:nv=151+d; 
        break;
        case 7:nv=181+d; 
        break;
        case 8:nv=212+d; 
        break;
        case 9:nv=243+d; 
        break;
        case 10:nv=273+d; 
        break;
        case 11:nv=304+d; 
        break;
        case 12:nv=334+d; 
        break;
    }
    printf("%d", nv);
    return 0;
}