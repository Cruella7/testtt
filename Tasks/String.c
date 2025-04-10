#include <stdio.h>
#include <ctype.h>


void invert(char* inputString) {
    for (int i = 0; inputString[i] != '\0'; ++i) {
        if (islower(inputString[i])) {
            inputString[i] = toupper(inputString[i]);
        } else if (isupper(inputString[i])) {
            inputString[i] = tolower(inputString[i]);
        }
    }
}

int main() {
    const int maxStringLength = 1000;
    char inputString[maxStringLength];

    printf("Введите строку: ");
    if (fgets(inputString, sizeof(inputString), stdin) == NULL) {
        fprintf(stderr, "Ошибка ввода строки\n");
        return 1;
    }

   
    for (int i = 0; inputString[i] != '\0'; ++i) {
        if (inputString[i] == '\n') {
            inputString[i] = '\0';
            break;
        }
    }

    invert(inputString);
    printf("%s\n", inputString);

    return 0;
}
