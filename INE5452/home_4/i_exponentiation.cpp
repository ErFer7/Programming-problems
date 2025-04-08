#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int calculation_count;

    cin >> calculation_count;

    for (int i = 0; i < calculation_count; i++) {
        long long a, b;
        const long long m = 1000000007;

        cin >> a >> b;

        a %= m;
        long long result = 1;
        while (b > 0) {
            if (b & 1) {
                result = result * a % m;
            }
            a = a * a % m;
            b >>= 1;
        }

        cout << result % 1000000007 << endl;
    }

    return 0;
}