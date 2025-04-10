/*Определить структурный тип adress (улица, дом, квартира).
Ввести указатель на тип adress. Выделить память для хранения информа-ции. 
Проинициализировать, вывести на экран.
Арутюнян С.К. 32ИС-21*/

#include <stdio.h>
#include <stdlib.h>

struct Address {
    char street[50];   
    int house;   
    int apartment; 
};

int main() {
    struct Address* ptrAddress = (struct Address*)malloc(sizeof(struct Address));

    if (ptrAddress == NULL) {
        printf("Ошибка выделения памяти.\n");
        return 1;
    }

    printf("Введите улицу: ");
    scanf("%49s", ptrAddress->street);  
    printf("Введите номер дома: ");
    scanf("%d", &ptrAddress->house);
    printf("Введите номер квартиры: ");
    scanf("%d", &ptrAddress->apartment);

    printf("\nИнформация об адресе:\n");
    printf("Улица: %s\n", ptrAddress->street);
    printf("Дом: %d\n", ptrAddress->house);
    printf("Квартира: %d\n", ptrAddress->apartment);

    free(ptrAddress);

    return 0;
}
