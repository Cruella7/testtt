#include <stdio.h>
#include <string.h>
#include "bus_data.h"

void printTotalPassengers() {
    int totalPassengers = 0;
    for (int i = 0; i < num_buses; i++) {
        totalPassengers += buses[i].passengers;
    }
    printf("Общее количество пассажиров: %d\n", totalPassengers);
}
