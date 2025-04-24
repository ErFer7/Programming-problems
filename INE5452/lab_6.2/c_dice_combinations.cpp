#include <iostream>

#define MOD 1000000007

using std::cin;
using std::cout;
using std::endl;

int main() {
    int dice_sum;

    cin >> dice_sum;

    int ways[dice_sum + 1];
    ways[0] = 1;

    for (int i = 1; i <= dice_sum; i++) {
        ways[i] = 0;

        for (int die = 1; die <= 6; die++) {
            if (i - die >= 0) {
                ways[i] = (ways[i] + ways[i - die]) % MOD;
            }
        }
    }

    cout << ways[dice_sum] << endl;
}