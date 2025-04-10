#include <stdio.h>
#include <stdlib.h>

double calculate_product(double A, double B, double C) {
    double AC = abs(C - A);
    double BC = abs(B - C);
    double product = AC * BC;
    return product;
}

int main() {
    double A = 2.0;
    double B = 2.0;
    double C = 8.0;

    double result = calculate_product(A, B, C);

    printf("%lf\n", result);

    return 0;
}
