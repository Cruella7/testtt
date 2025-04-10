#include <stdio.h>

int main() {
    int number;
    
    printf("Ввод: ");
    scanf("%d", &number);

    int t = (number / 1000) % 10;

    printf("%d\n", t);

    return 0;
}
