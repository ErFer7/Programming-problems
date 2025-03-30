#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int tape_length;

    while(cin >> tape_length) {
        int track_count;

        cin >> track_count;

        int tracks[track_count];

        for (int i = 0; i < track_count; i++) {
            cin >> tracks[i];
        }

        int max_length = 0;
        unsigned int max_length_bits = 0;

        for (unsigned int bits = 0; bits < 1 << track_count; bits++) {
            int length = 0;

            for (int i = 0; i < track_count; i++) {
                if (bits & (1 << i)) {
                    length += tracks[i];
                }
            }
            
            if (length <= tape_length && length > max_length) {
                max_length = length;
                max_length_bits = bits;

                if (length == tape_length) {
                    break;
                }
            }
        }

        for (int i = 0; i < track_count; i++) {
            if (max_length_bits & (1 << i)) {
                cout << tracks[i] << " ";
            }
        }

        cout << "sum:" << max_length << endl;
    }

    return 0;
}