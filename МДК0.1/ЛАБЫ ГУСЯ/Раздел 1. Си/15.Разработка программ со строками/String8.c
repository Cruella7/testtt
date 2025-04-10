/** String8. Дано целое число N (> 0) и символ C. Вывести строку длины N,
которая состоит из символов C. */
#include <stdio.h>
#define LEN 1000
int main() {
    char s[LEN];
    int n;
    char c;
    scanf("%d %c", &n, &c);
    int i;
    for (i = 0; i < n; ++i)
        s[i] = c;
    s[i] = '\0';
    printf("%s\n", s);
    return 0;
}
