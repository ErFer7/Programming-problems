#include <cmath>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int test_count;

    cin >> test_count;

    for (int i = 0; i < test_count; i++) {
        int a, b, c;

        cin >> a >> b >> c;

        bool solution_exists = false;

        for (int x = -100; x <= 100; x++) {
            if (solution_exists) {
                break;
            }

            for (int y = -100; y <= 100; y++) {
                int z = a - x - y;

                if (x * y * z == b && std::pow(x, 2) + std::pow(y, 2) + std::pow(z, 2) == c && x != y && x != z && y != z) {
                    cout << x << " " << y << " " << z << endl;
                    solution_exists = true;
                    break;
                }
            }
        }

        if (!solution_exists) {
            cout << "No solution." << endl;
        }
    }

    return 0;
}