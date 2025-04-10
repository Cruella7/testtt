#include<stdio.h>
int main()
{
    int fahr, Celsius;
    int lower, upper, step;
    
    printf("Шкала Цельсия\n");
    lower = 0;
    upper = 300;
    step = 20;
    
    fahr = lower;
    while(fahr <= upper){
        Celsius = 5 * (fahr-32) / 9;
        printf("%3d\t%6d\n", fahr, Celsius);
        fahr = fahr + step;
    }
    
}
