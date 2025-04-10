#include <stdio.h>

int opredelitel(int a, int b, int c) {
    if (a == b) {
        return 3;
    } else if (a == c) {
        return 2;
    } else {
        return 1;
    }
}

int main() {
    int n1, n2, n3;
    
    printf("1: ");
    scanf("%d", &n1);
    
    printf("2: ");
    scanf("%d", &n2);
    
    printf("3: ");
    scanf("%d", &n3);

    int result = opredelitel(n1, n2, n3);
    printf("%d\n", result);

    return 0;
}
