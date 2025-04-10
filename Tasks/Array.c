#include <stdio.h>

int find_element(int A[], int size) {
    int A10 = A[size - 1];
    for (int i = 0; i < size; i++) {
        if (A[i] < A10) {
            return A[i];
        }
    }
    return 0;
}

int main() {
    int A[] = {5, 8, 12, 4, 7, 10, 15, 6, 20, 21};
    int size = sizeof(A) / sizeof(A[0]);

    int result = find_element(A, size);

    printf("%d\n", result);

    return 0;
}
