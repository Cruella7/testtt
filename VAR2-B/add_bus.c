#include <stdio.h>
#include <string.h>
#include "bus_data.h"

void addBus(const char *number, const char *station, int passengers) {
    if (num_buses < MAX_BUSES) {
        strcpy(buses[num_buses].number, number);
        strcpy(buses[num_buses].station, station);
        buses[num_buses].passengers = passengers;
        num_buses++;
        printf("Рейс успешно добавлен.\n");
    } else {
        printf("Достигнуто максимальное количество рейсов.\n");
    }
}
