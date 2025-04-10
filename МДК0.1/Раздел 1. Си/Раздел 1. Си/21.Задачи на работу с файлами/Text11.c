/** М. Э. Абрамян. 1000 ЗАДАЧ ПО ПРОГРАММИРОВАНИЮ, Ростов-на-Дону 2004.
Text11. Дан текстовый файл. Продублировать в нем все пустые строки.
Решение: Гусятинер Л.Б., 22.09.2020
*/

#include <stdio.h>
#include <unistd.h>
#define MAXLEN 80

int main() {
    char *fname1 = "Text11.txt";
    char *fname2 = "tmp.txt";
    FILE *f1 = fopen(fname1, "r");
    FILE *f2 = fopen(fname2, "w");
    char s[MAXLEN];
    while (fgets(s, MAXLEN + 1, f1) != NULL) {
        fputs(s, f2);
        if (s[0] == '\n')
            fputs(s, f2);
    }
    fclose(f2);
    fclose(f1);
    remove(fname1);
    rename(fname2, fname1);

    getchar();

    return 0;
}
