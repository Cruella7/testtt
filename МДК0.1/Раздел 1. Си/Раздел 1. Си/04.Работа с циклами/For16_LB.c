/** For16. ���� ������������ ����� A � ����� ����� N (> 0). ��������� ���� ����,
������� ��� ����� ������� ����� A �� 1 �� N. */
#include <stdio.h>
int main() {
    int n;
    scanf("%d", &n);
    double a;
    scanf("%lf", &a);
    double b = 1;
    int i = 1;
    while (i <= n) {
        b = b * a;
        printf("%.2f ", b);
        i = i + 1;
    }
    return 0;
}
