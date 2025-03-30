#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int test_count;

    cin >> test_count;

    for (int i = 0; i < test_count; i++) {
        int target_length, bar_count;

        cin >> target_length;
        cin >> bar_count;

        int bars[bar_count];

        for (int j = 0; j < bar_count; j++) {
            cin >> bars[j];
        }

        if (target_length == 0) {
            cout << "YES" << endl;
            continue;
        }

        bool solution_exists = false;

        for (unsigned int bits = 0; bits < 1 << bar_count; bits++) {
            int length = 0;

            for (int j = 0; j < bar_count; j++) {
                if (bits & (1 << j)) {
                    length += bars[j];
                }
            }

            if (length == target_length) {
                solution_exists = true;
                break;
            }
        }

        cout << (solution_exists ? "YES" : "NO") << endl;
    }

    return 0;
}