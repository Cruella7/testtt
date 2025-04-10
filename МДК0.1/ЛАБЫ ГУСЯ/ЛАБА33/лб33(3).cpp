#include <iostream>
int main() {
    int a, b, c;
    std:: cout << "Введите три числа: ";
    std:: cin >> a >> b >> c;
    int m = std:: max(a, std:: max(b, c)); 
    int n = std:: max(std:: min(a, b), std::max(std::min(a, c), std::min(b, c))); 
    int sum = m + n; 
    std:: cout << "Сумма двух наибольших чисел: " << sum << std:: endl;
    return 0;
}