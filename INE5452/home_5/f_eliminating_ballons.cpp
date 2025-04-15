#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int ballon_count;
    cin >> ballon_count;

    int arrow_count = 0;
    int arrows[1000000] = {0};

    for (int i = 0; i < ballon_count; i++) {
        int height;
        cin >> height;
        height--;

        if (arrows[height] > 0) {
            arrows[height]--;
        } else {
            arrow_count++;
        }

        if (height > 0) {
            arrows[height - 1]++;
        }
    }

    cout << arrow_count << endl;

    return 0;
}