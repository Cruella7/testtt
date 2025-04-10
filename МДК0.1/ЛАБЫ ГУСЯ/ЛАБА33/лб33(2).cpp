#include <iostream>
int main() {
    int n;
    std:: cout << "n: ";
    std:: cin >> n;

    if (n > 0) {
        if (n % 2 == 0) {
            std:: cout << "положительное четное число" << std:: endl;
        } else {
            std:: cout << "положительное нечетное число" << std:: endl;
        }
    } else if (n < 0) {
        if (n % 2 == 0) {
            std:: cout << "oтрицательное четное число " << std:: endl;
        } else {
            std:: cout << "oтрицательное нечетное число" << std:: endl;
        }
    } else {
        std:: cout << "нулевое число" << std:: endl;
    }

    return 0;
}