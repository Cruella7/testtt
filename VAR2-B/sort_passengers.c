#include <stdio.h>
#include <string.h>
#include "bus_data.h"

void sortByPassengers() {
    for (int i = 0; i < num_buses - 1; i++) {
        for (int j = 0; j < num_buses - i - 1; j++) {
            if (buses[j].passengers > buses[j + 1].passengers) {
                BusInfo temp = buses[j];
                buses[j] = buses[j + 1];
                buses[j + 1] = temp;
            }
        }
    }
    printf("Рейсы в сортировке по количеству пассажиров:\n");
    for (int i = 0; i < num_buses; i++) {
        printf("%s %s %d\n", buses[i].number, buses[i].station, buses[i].passengers);
    }
}
