#include <stdio.h>
#include <math.h>
#define MAXN 1000

int main() {
    double v[MAXN];
    int n;
    scanf ("%d", &n);
    for (int i = 0; i < n; ++i)
        scanf("%lf", &v[i]);
    for (int i = 0; i < n; ++i)
        printf("%5.2f\n", pow(v[i], (i+1)));

   return 0;
}
