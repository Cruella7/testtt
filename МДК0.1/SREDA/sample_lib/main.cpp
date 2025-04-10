#include <iostream>
#include "sample_module.h"

using namespace std;

int main()
{
    int n1, n2, n;
    cout << "enter n1: ";
    cin >> n1;
    cout << "enter n2: ";
    cin >> n2;
    n = SampleAddInt(n1,n2);
    cout << "the result is: " << n << endl;
    return 0;
}
