#include <stdio.h>
#include <math.h>

float RadToDeg(float R) {
    if (0 <= R && R < 2 * M_PI) {
        return R * (180 / M_PI);
    } else {
        return -1; // Ошибка
    }
}

int main() {
    float ugly[] = {0.5, 1.0, 1.5, 2.0, 2.5};
    int size = sizeof(ugly) / sizeof(ugly[0]);

    for (int i = 0; i < size; ++i) {
        float radians = ugly[i];
        float angle_in_degrees = RadToDeg(radians);

        if (angle_in_degrees != -1) {
            printf("%.2f радиан = %.2f градусов\n", radians, angle_in_degrees);
        } else {
            printf("Ошибка: %.2f не входит в диапазон [0, %.2f)\n", radians, 2 * M_PI);
        }
    }

    return 0;
}
