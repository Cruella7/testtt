#include <stdio.h>

float find_local_minimum(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Ошибка открытия файла");
        return -1;
    }

    float number;
    float previous_number = 0.0;
    float current_number;

    while (fscanf(file, "%f", &current_number) == 1) {
        if (previous_number > current_number && current_number < fscanf(file, "%f", &number)) {
            fclose(file);
            return current_number;
        }
        previous_number = current_number;
    }

    fclose(file);
    return -1;
}

int main() {
    const char *filename = "цифры.txt";  // Замените 'ваш_файл.txt' на путь к вашему файлу
    float result = find_local_minimum(filename);

    if (result != -1) {
        printf("Локальный минимум: %f\n", result);
    } else {
        printf("Локальный минимум не найден.\n");
    }

    return 0;
}
