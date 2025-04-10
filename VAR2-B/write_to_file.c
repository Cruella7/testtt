#include <stdio.h>
#include <string.h>
#include "bus_data.h"

void writeToOutFile() {
    // Открытие файла для записи результатов
    FILE *out_file = fopen("out.txt", "w");
    if (out_file == NULL) {
        printf("Ошибка открытия файла out.txt\n");
        return;
    }

    // Открытие файла для чтения исходных данных
    FILE *in_file = fopen("in.txt", "r");
    if (in_file == NULL) {
        printf("Ошибка открытия файла in.txt\n");
        fclose(out_file);
        return;
    }

    // Чтение данных из файла и запись в файл out.txt
    fprintf(out_file, "Номер автобуса | Станция | Количество пассажиров\n");
    while (fscanf(in_file, "%s %s %d", buses[num_buses].number, buses[num_buses].station, &buses[num_buses].passengers) == 3) {
        fprintf(out_file, "%s %s %d\n", buses[num_buses].number, buses[num_buses].station, buses[num_buses].passengers);
        num_buses++; // Увеличение счетчика автобусов
    }

    // Закрытие файлов
    fclose(in_file);
    fclose(out_file);

    printf("Результаты успешно записаны в файл out.txt.\n");
}
