#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int stone_count;
    cin >> stone_count;

    int stones_heights[stone_count];

    for (int i = 0; i < stone_count; i++) {
        int stones_height;
        cin >> stones_height;

        stones_heights[i] = stones_height;
    }

    int costs[stone_count];

    costs[0] = 0;
    costs[1] = std::abs(stones_heights[1] - stones_heights[0]);

    for (int i = 2; i < stone_count; i++) {
        int current_stone_height = stones_heights[i];
        int first_previous_height = stones_heights[i - 1];
        int second_previous_height = stones_heights[i - 2];

        int first_previous_cost = costs[i - 1] + std::abs(first_previous_height - current_stone_height);
        int second_previous_cost = costs[i - 2] + std::abs(second_previous_height - current_stone_height);

        costs[i] = std::min(first_previous_cost, second_previous_cost);
    }

    cout << costs[stone_count - 1] << endl;

    return 0;
}
