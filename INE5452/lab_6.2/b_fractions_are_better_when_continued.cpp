#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int fibonacci(int n) {
    if (n < 2) {
        return 1;
    }

    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int number;

    cin >> number;

    cout << fibonacci(number) << endl;

    return 0;
}