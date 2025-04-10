/* Робот может перемещаться в четырех направлениях («С» — север,
«З» — запад, «Ю» — юг, «В» — восток) и принимать три цифровые ко-
манды: 0 — продолжать движение, 1 — поворот налево, −1 — поворот
направо. Дан символ C — исходное направление робота и целое число N
— посланная ему команда. Вывести направление робота после выполне-
ния полученной команды.*/
/* LB. Приняты обозначения N (Север), E (Восток), S (Юг), W (Запад) 27.01.2023 */

#include <stdio.h>

int main()
{
    int n;
    char a;
    scanf("%c", &a);
    scanf("%d", &n);
    switch(a) {
    case 'N':
        switch(n) {
        case 0:
            printf("Север");
            break;
            
        case 1:
            printf("Запад");
            break;
            
        case -1:
            printf("Восток");
            break;
        }
        break;
        
    case 'W':
        switch(n) {
        case 0:
            printf("Запад");
            break;
            
        case 1:
            printf("Юг");
            break;
            
        case -1:
            printf("Север");
            break;
        }
        break;
        
    case 'S':
        switch(n) {
        case 0:
            printf("Юг");
            break;
            
        case 1:
            printf("Восток");
            break;
            
        case -1:
            printf("Запад");
            break;
        }
        break;
        
    case 'E':
        switch(n) {
        case 0:
            printf("Восток");
            break;
            
        case 1:
            printf("Север");
            break;
            
        case -1:
            printf("Юг");
            break;
        }
        break;
    }
    
    return 0;
}
