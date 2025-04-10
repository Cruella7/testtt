/** �. �. �������. 1000 ����� �� ����������������, ������-��-���� 2004.
Matrix1. ���� ����� ������������� ����� M � N. ������������ �������������
������� ������� M * N, � ������� ��� �������� i-� ������ ����� ��������
10*i (i = 1, �, m).
������� ��������� �.�., 10.2012 */

#include <stdio.h>
const size_t MAXM = 10;
const size_t MAXN = 10;

int main() {
    int i, j;
    int a[MAXM][MAXN];
    int m, n;

    scanf("%d%d", &m, &n);
    for (i = 0; i < m; ++i) {
        for (j = 0; j < n; ++j) {
            a[i][j] = 10 * i;
        }
    }

    for (i = 0; i < m; ++i) {
        for (j = 0; j < n; ++j)
            printf("%4d", a[i][j]);
        printf("\n");
    }
    getchar();
    return 0;
}
