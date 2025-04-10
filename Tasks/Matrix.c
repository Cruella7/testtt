#include <stdio.h>

#define MAX_ROWS 100
#define MAX_COLS 100

int main() {
    int M, N, K;
    int matrix[MAX_ROWS][MAX_COLS];

    printf("M: ");
    scanf("%d", &M);

    printf("N: ");
    scanf("%d", &N);

    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            printf("Введите элемент матрицы (%d, %d): ", i + 1, j + 1);
            scanf("%d", &matrix[i][j]);
        }
    }

    printf("Введите номер столбца K: ");
    scanf("%d", &K);

    if (1 <= K && K <= N) {
        int column_sum = 0;
        int column_product = 1;

        for (int i = 0; i < M; ++i) {
            column_sum += matrix[i][K - 1];
            column_product *= matrix[i][K - 1];
        }

        printf("Сумма элементов %d-го столбца: %d\n", K, column_sum);
        printf("Произведение элементов %d-го столбца: %d\n", K, column_product);
    } else {
        printf("Ошибка\n");
    }

    return 0;
}
