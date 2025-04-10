/*Ввести с клавиатуры номер дня недели. 
Вывести на экран его на-
звание. Использовать перечисления (enum).
Арутюнян С.К. 32ИС-21*/
#include <stdio.h>

enum Days {
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Satuday,
    Sunday
};

int main() {
    int dayNumber;

    printf("Введите номер дня недели (1-7): ");
    scanf("%d", &dayNumber);

    if (dayNumber < 1 || dayNumber > 7) {
        printf("Некорректный номер дня недели.\n");
        return 1; 
    }

    enum Days day = dayNumber - 1;

    switch (day) {
        case Monday:
            printf("Понедельник\n");
            break;
        case Tuesday:
            printf("Вторник\n");
            break;
        case Wednesday:
            printf("Среда\n");
            break;
        case Thursday:
            printf("Четверг\n");
            break;
        case Friday:
            printf("Пятница\n");
            break;
        case Satuday:
            printf("Суббота\n");
            break;
        case Sunday:
            printf("Воскресенье\n");
            break;
    }
    
    return 0;
}