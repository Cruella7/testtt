//Вывести сначала чётные элементы массива, а затем нечётные.
//Входные данные: Первая строка число N, (N > 0) - длина массива. 
//Длина массива не более 100 элементов. Вторая строка N натуральных чисел, 
//записанных через пробел. Выходные данные: Элементы массива,
//упорядоченные соответствующим образом. Сначала чётные элементы массива в том порядке, 
//как они встречаются в массиве, затем нечётные элементы массива в том порядке, 
//как они встречаются в массиве.

#include <stdio.h>
#define xxx 100
int main() {
    int n, a, ss[xxx];
    scanf("%d", &n);
    
    for (int i = 0; i<n ; i++)
    {
        scanf("%d", &ss[i]);
    }
    
    for (int i = 0; i<n ; i++)
    {
         if (ss[i]%2==0) printf("%d ", ss[i]);    
    } 


    for (int i = 0; i<n ; i++)
    {
         if (ss[i]%2!=0) printf("%d ", ss[i]);    
    }  
    

    return 0;
}


