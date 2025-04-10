//. Факториал. Напишите функцию с именем factorial, 
//которая вычисляет факториал числа, переданного ей в качестве аргумента.
//Входные данные: Одно целое неотрицательное число N, (N < 13).
//Выходные данные: Одно целое число, факториал исходного числа.
#include <stdio.h>
 
int factorial(int s)
{
   int n=1, i;
   if(s > 1){
   for(i=1; i <= s; i++) 
   n*=i;

return n;
}
   else if(s <= 1) 
return 1;
}     


#include <stdio.h>
int main()
{
   int a;
   scanf("%d", &a); 

   printf ("%d", factorial(a));

return 0;
}
