#include <stdio.h>

#define MAX_SIZE 100

void Chessboard(int M, int N, int A[MAX_SIZE][MAX_SIZE]) {
    for (int i = 1; i <= M; ++i) {
        for (int j = 1; j <= N; ++j) {
            A[i - 1][j - 1] = (i + j) % 2;
        }
    }
}

int main() {
    int M, N;
    printf("Введите M: ");
    scanf("%d", &M);
    printf("Введите N: ");
    scanf("%d", &N);

    int matritsa_custom[MAX_SIZE][MAX_SIZE];

    Chessboard(M, N, matritsa_custom);

    printf("Результирующая матрица:\n");
    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            printf("%d ", matritsa_custom[i][j]);
        }
        printf("\n");
    }

    return 0;
}
