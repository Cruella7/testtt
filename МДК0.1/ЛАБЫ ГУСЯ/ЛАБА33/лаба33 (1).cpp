#include <iostream>


int main() {
    int n;
    std::cout << "n: ";
    std::cin >> n;

    if (n > 0) {
        n += 1;
    } else if (n < 0) {
        n-= 2;
    } else {
        n = 10;
    }

   std:: cout << "result:" << n << std::endl;
    return 0;
}
