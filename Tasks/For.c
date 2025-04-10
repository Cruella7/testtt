#include <stdio.h>

float calculate_expression(float X, int N) {
    float result = 0;
    int sign = 1;

    for (int i = 0; i <= N; ++i) {
        result += sign * pow(X, i);
        sign *= -1;
    }

    return result;
}

int main() {
    float V;
    int N;

    printf("V: ");
    scanf("%f", &V);

    printf("N (> 0): ");
    scanf("%d", &N);

    if (N > 0) {
        float result = calculate_expression(V, N);
        printf("Значение: %f\n", result);
    } else {
        printf("Неправильный ввод.\n");
    }

    return 0;
}
