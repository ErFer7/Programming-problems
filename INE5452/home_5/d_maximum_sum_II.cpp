#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    while (true) {
        int number_count;
        cin >> number_count;

        if (number_count == 0) {
            break;
        }

        bool is_only_zeroes = true;

        for (int i = 0; i < number_count; i++) {
            int number;
            cin >> number;

            if (number > 0) {
                if (is_only_zeroes) {
                    cout << number;
                } else {
                    cout << ' ' << number;
                }

                is_only_zeroes = false;
            }
        }

        if (is_only_zeroes) {
            cout << 0 << endl;
        } else {
            cout << endl;
        }
    }

    return 0;
}