#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int test_count;

    cin >> test_count;

    for (int i = 0; i < test_count; i++) {
        int field_size;
        std::string field;

        cin >> field_size >> field;

        int scarecrows = 0;

        if (field_size < 4) {
            for (int j = 0; j < field_size; j++) {
                if (field[j] == '.') {
                    scarecrows = 1;
                    break;
                }
            }
        } else {
            for (int j = 1; j < field_size; j++) {
                char spot_left = field[j - 1];

                if (j == field_size - 1 && field[j] == '.') {
                    scarecrows++;
                } else if (spot_left == '.') {
                    field[j] = '#';

                    if (j + 1 < field_size) {
                        field[j + 1] = '#';
                    }

                    scarecrows++;
                }
            }
        }

        cout << "Case " << i + 1 << ": " << scarecrows << endl;
    }

    return 0;
}