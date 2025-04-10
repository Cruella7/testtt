#include <stdio.h>
#include <string.h>


void processFile(const char* filePath, int kValue) {
    FILE* file = fopen(filePath, "r");
    if (file == NULL) {
        fprintf(stderr, "Файл не найден.\n");
        return;
    }

    char line[1000]; 

    FILE* outputFile = fopen("temp.txt", "w"); 
    if (outputFile == NULL) {
        fclose(file);
        fprintf(stderr, "Не удалось создать временный файл.\n");
        return;
    }

    
    while (fgets(line, sizeof(line), file) != NULL) {
        if (strlen(line) >= kValue) {
            fputs(line + kValue, outputFile); 
        }
    }

    fclose(file);
    fclose(outputFile);

    
    remove(filePath);
    rename("Text.txt", filePath);

    printf("Успешно удалены первые %d символов из каждой строки файла.\n", kValue);
}

int main() {
    char filePath[256];
    int kValue;

    printf("Введите имя файла: ");
    scanf("%255s", filePath);

    printf("Введите количество символов для удаления: ");
    scanf("%d", &kValue);

    processFile(filePath, kValue);

    return 0;
}
