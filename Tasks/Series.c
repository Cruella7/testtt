#include <stdio.h>
#include <stdlib.h>


void uniqueElementsInOrder(int N, int* numbers) {
    
    int* visited = (int*)malloc(N * sizeof(int));
    if (visited == NULL) {
        perror("Ошибка выделения памяти");
        exit(EXIT_FAILURE);
    }

    
    for (int i = 0; i < N; ++i) {
        visited[i] = 0;
    }

    printf("Различные элементы в порядке возрастания:\n");

    for (int i = 0; i < N; ++i) {
        if (!visited[i]) {
            printf("%d\n", numbers[i]);

           
            for (int j = i + 1; j < N; ++j) {
                if (numbers[j] == numbers[i]) {
                    visited[j] = 1;
                }
            }
        }
    }

    
    free(visited);
}

int main() {
    int N;

    printf("N: ");
    if (scanf("%d", &N) != 1 || N <= 0) {
        fprintf(stderr, "Ошибка ввода N\n");
        exit(EXIT_FAILURE);
    }

    int* numbers = (int*)malloc(N * sizeof(int));
    if (numbers == NULL) {
        perror("Ошибка выделения памяти");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < N; ++i) {
        printf("Введите число #%d: ", i + 1);
        if (scanf("%d", &numbers[i]) != 1) {
            fprintf(stderr, "Ошибка ввода числа\n");
            free(numbers);
            exit(EXIT_FAILURE);
        }
    }

    uniqueElementsInOrder(N, numbers);

    
    free(numbers);

    return 0;
}
