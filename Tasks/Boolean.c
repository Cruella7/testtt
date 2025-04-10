#include <stdio.h>

int has_duplicate(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (arr[i] == arr[j]) {
                return 1; // Есть совпадающие числа
            }
        }
    }
    return 0; // Нет совпадающих чисел
}

int main() {
    int num[] = {2, 2, 8};
    int size = sizeof(num) / sizeof(num[0]);

    if (has_duplicate(num, size)) {
        printf("Среди трех данных целых чисел есть хотя бы одна пара совпадающих.\n");
    } else {
        printf("Среди трех данных целых чисел нет совпадающих пар.\n");
    }

    return 0;
}
