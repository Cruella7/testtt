
#include <iostream>
#include <climits>
#include <cfloat>

int main() {
    std::cout << "Size of int: " << sizeof(int) * CHAR_BIT << " bits" << std::endl;
    std::cout << "Size of float: " << sizeof(float) * CHAR_BIT << " bits" << std::endl;
    std::cout << "Size of char: " << sizeof(char) * CHAR_BIT << " bits" << std::endl;
    std::cout << "Size of bool: " << sizeof(bool) * CHAR_BIT << " bits" << std::endl;
    std::cout << "Size of size_t: " << sizeof(std::size_t) * CHAR_BIT << " bits" << std::endl;
    return 0;
}