#include <iostream>
#include <unordered_map>

int main() {
    long catalan_numbers[20];
    std::unordered_map<long, long> catalan_map;

    catalan_numbers[0] = 1;
    catalan_map[catalan_numbers[0]] = 0;

    for (long i = 1; i < 20; i++) {
        catalan_numbers[i] = ((4 * i - 2) * catalan_numbers[i - 1]) / (i + 1);
        catalan_map[catalan_numbers[i]] = i;
    }

    while (true) {
        long max_tree_count;

        if (!(std::cin >> max_tree_count)) {
            break;
        }

        std::cout << catalan_map[max_tree_count] << std::endl;
    }

    return 0;
}
