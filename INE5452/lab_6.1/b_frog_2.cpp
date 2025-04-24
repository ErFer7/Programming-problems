#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int stone_count, jump_capacity;
    cin >> stone_count >> jump_capacity;

    int stones_heights[stone_count];

    for (int i = 0; i < stone_count; i++) {
        int stones_height;
        cin >> stones_height;

        stones_heights[i] = stones_height;
    }

    int costs[stone_count];

    costs[0] = 0;

    for (int i = 1; i < stone_count; i++) {
        int min_cost = INT32_MAX;

        for (int j = i - jump_capacity > 0 ? i - jump_capacity : 0; j < i; j++) {
            int cost = costs[j] + std::abs(stones_heights[j] - stones_heights[i]);

            if (min_cost > cost) {
                min_cost = cost;
            }
        }

        costs[i] = min_cost;
    }

    cout << costs[stone_count - 1] << endl;

    return 0;
}
