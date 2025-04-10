#include <stdio.h>
#include "bus_data.h"

// Определение функции для загрузки данных из файла
void loadFromFile() {
    FILE *in_file = fopen("in.txt", "r");
    if (in_file == NULL) {
        printf("Ошибка открытия файла in.txt\n");
        return;
    }

    while (fscanf(in_file, "%s %s %d", buses[num_buses].number, buses[num_buses].station, &buses[num_buses].passengers) == 3) {
        num_buses++; // Увеличение счетчика автобусов
    }

    fclose(in_file);
}
