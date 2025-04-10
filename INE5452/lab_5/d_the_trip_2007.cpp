#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using std::cin;
using std::cout;
using std::endl;

int main() {
    while (true) {
        int bag_count;

        cin >> bag_count;

        if (bag_count == 0) {
            break;
        }

        int bags[bag_count];
        std::unordered_map<int, int> bag_repetition;

        for (int i = 0; i < bag_count; i++) {
            cin >> bags[i];

            bag_repetition[bags[i]]++;
        }

        std::sort(
            bags, 
            bags + bag_count,
            [](const int a, const int b) { return a > b; }
        );

        int least_repeated = std::max_element(
            bag_repetition.begin(),
            bag_repetition.end(),
            [](std::pair<int, int> a, std::pair<int, int> b) {
                return a.second < b.second;
            })->second;

        std::vector<std::vector<int>> bag_containers;

        for (int i = 0; i < least_repeated; i++) {
            std::vector<int> vec;

            bag_containers.push_back(vec);
        }

        int bag_containers_index = 0;

        for (int i = 0; i < bag_count; i++) {
            bag_containers[bag_containers_index].push_back(bags[i]);

            bag_containers_index = (bag_containers_index + 1) % least_repeated;
        }

        cout << bag_containers.size() << endl;

        for (int i = bag_containers.size() - 1; i >= 0; i--) {
            for (int j = 0; j < bag_containers[i].size(); j++) {
                if (j == bag_containers[i].size() - 1) {
                    cout << bag_containers[i][j] << endl;
                } else {
                    cout << bag_containers[i][j] << ' ';
                }
            }
        }

        cout << endl;
    }

    return 0;
}