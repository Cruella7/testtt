#include <stdio.h>
#include <string.h>
#include "bus_data.h"

void editBus() {
    char numberToEdit[MAX_LEN];
    printf("Введите номер автобуса для редактирования: ");
    scanf("%s", numberToEdit);

    int found = 0;
    for (int i = 0; i < num_buses; i++) {
        if (strcmp(buses[i].number, numberToEdit) == 0) {
            printf("Введите новые данные для рейса (номер, станция, количество пассажиров): ");
            scanf("%s %s %d", buses[i].number, buses[i].station, &buses[i].passengers);
            found = 1;
            printf("Данные рейса успешно изменены.\n");
            break;
        }
    }
    if (!found) {
        printf("Рейс с указанным номером не найден.\n");
    }
}