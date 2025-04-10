#include <stdio.h>
#include <string.h>
#include "bus_data.h"

void removeBus() {
    char numberToRemove[MAX_LEN];
    printf("Введите номер автобуса для удаления: ");
    scanf("%s", numberToRemove);

    int found = 0;
    for (int i = 0; i < num_buses; i++) {
        if (strcmp(buses[i].number, numberToRemove) == 0) {
            for (int j = i; j < num_buses - 1; j++) {
                buses[j] = buses[j + 1];
            }
            num_buses--;
            found = 1;
            printf("Рейс успешно удален.\n");
            break;
        }
    }
    if (!found) {
        printf("Рейс с указанным номером не найден.\n");
    }
}