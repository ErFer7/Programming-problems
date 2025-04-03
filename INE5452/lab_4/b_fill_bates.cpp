#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;

int main() {
    std::string entry;

    cin >> entry;

    std::unordered_map<char, std::vector<int>> char_map;

    for (int i = 0; i < entry.length(); i++) {
        char_map[entry[i]].push_back(i);
    }

    int query_count;

    cin >> query_count;

    for (int i = 0; i < query_count; i++) {
        bool valid = true;
        std::string query;

        cin >> query;

        std::vector<int> candidate_positions;

        for (int j = 0; j < query.length(); j++) {
            char c = query[j];
            int last_position = candidate_positions.empty() ? -1 : candidate_positions.back();

            auto position = std::upper_bound(char_map[c].begin(), char_map[c].end(), last_position);
    
            if (position == char_map[c].end()) {
                valid = false;
                break;
            }

            candidate_positions.push_back(*position);
        }

        if (valid) {
            cout << "Matched " << candidate_positions[0] << ' ' << candidate_positions.back() << endl;
        } else {
            cout << "Not matched" << endl;
        }
    }

    return 0;
}