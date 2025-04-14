#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int test = 0;

    while (true) {
        test++;

        int bachelor_count, spinster_count;

        cin >> bachelor_count >> spinster_count;

        if (bachelor_count == 0) {
            break;
        }

        int bachelors[bachelor_count];
        int spinsters[spinster_count];
        int youngest_bachelor = 61;

        for (int i = 0; i < bachelor_count; i++) {
            cin >> bachelors[i];

            if (bachelors[i] < youngest_bachelor) {
                youngest_bachelor = bachelors[i];
            }
        }

        for (int i = 0; i < spinster_count; i++) {
            cin >> spinsters[i];
        }

        if (bachelor_count <= spinster_count) {
            cout << "Case " << test << ": " << 0 << endl;
        } else {
            cout << "Case " << test << ": " << bachelor_count - spinster_count << ' ' << youngest_bachelor << endl;
        }
    }

    return 0;
}