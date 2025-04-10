//2. Напишите программу, которая выводит размеры типов
//int, float, char в байтах. 
//Каждое значение должно быть в отдельной строке в указанном порядке. 

#include <stdio.h>

int main()
{
  int intType;
  char chType;
  float flType;
  
    printf("Size of int is: %ld\n", // размер int

           sizeof(intType));

    printf("Size of char is: %ld\n", //размер char

           sizeof(chType));

    printf("Size of float is: %ld\n", //размер float

           sizeof(flType));
           

    return 0;
}
