#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int test_count;

    cin >> test_count;

    for (int i = 0; i < test_count; i++) {
        int rung_count;

        cin >> rung_count;

        int ladder[rung_count];

        int max_distance = 0;

        for (int j = 0; j < rung_count; j++) {
            cin >> ladder[j];

            if (j > 0) {
                int distance = ladder[j] - ladder[j - 1];

                if (distance > max_distance) {
                    max_distance = distance;
                }
            } else {
                max_distance = ladder[j];
            }
        }

        int lower = max_distance;
        int upper = ladder[rung_count - 1];
        int k = 0;

        do {
            int middle = (lower + upper) / 2;
            int test_k = middle;
            int position = 0;
            int index = 0;
            bool reached_top = true;

            do {
                if (ladder[index] - position == test_k) {
                    position = ladder[index];
                    index++;
                    test_k--;
                } else if (ladder[index] - position < test_k) {
                    position = ladder[index];
                    index++;
                } else {
                    reached_top = false;
                    break;
                }
            } while (index < rung_count);

            if (reached_top) {
                k = middle;
                upper = middle - 1;
            } else {
                lower = middle + 1;
            }
        } while (lower <= upper);

        cout << "Case " << i + 1 << ": " << k << endl;
    }

    return 0;
}