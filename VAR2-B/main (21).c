#include <stdio.h>
#include "bus_data.h"

extern BusInfo buses[MAX_BUSES];
extern int num_buses;

extern void addBus();
extern void removeBus();
extern void editBus();
extern void loadFromFile();
extern void printTotalPassengers();
extern void sortByPassengers();
extern void writeToOutFile();

int main() {
    int choice;

    do {
        printf("\nМеню:\n");
        printf("1. Добавить новый рейс\n");
        printf("2. Удалить рейс\n");
        printf("3. Редактировать рейс\n");
        printf("4. Все данные\n");
        printf("5. Вывести общее количество рейсов\n");
        printf("6. Вывести рейсы в сортировке по количеству пассажиров\n");
        printf("7. Записать результаты в файл\n");
        printf("8. Выход\n");
        printf("Выберите действие: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addBus();
                break;
            case 2:
                removeBus();
                break;
            case 3:
                editBus();
                break;
            case 4:
                loadFromFile();
                break;
            case 5:
                printTotalPassengers();
                break;
            case 6:
                sortByPassengers();
                break;
            case 7:
                writeToOutFile();
                break;
            case 8:
                printf("Выход...\n");
                break;
            default:
                printf("Некорректный ввод. Пожалуйста, введите число от 1 до 8.\n");
        }
    } while (choice != 8);

    return 0;
}
