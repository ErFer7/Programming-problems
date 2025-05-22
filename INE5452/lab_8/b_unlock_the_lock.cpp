#include <iostream>
#include <unordered_map>
#include <queue>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int test = 1;

    while (true) {
        int initial_code, final_code, button_count;
        cin >> initial_code >> final_code >> button_count;

        if (button_count == 0) {
            break;
        }

        int buttons[button_count];

        for (int i = 0; i < button_count; i++) {
            cin >> buttons[i];
        }

        std::queue<int> queue;
        std::unordered_map<int, int> parents;
        std::unordered_map<int, bool> visited;

        queue.push(initial_code);
        visited[initial_code] = true;
        bool is_final_code_found = false;

        while (!queue.empty() && !is_final_code_found) {
            int code = queue.front();
            queue.pop();

            for (int buttons : buttons) {
                int combination = (code + buttons) % 10000;

                if (!visited[combination]) {
                    queue.push(combination);
                    parents[combination] = code;
                    visited[combination] = true;

                    if (combination == final_code) {
                        is_final_code_found = true;
                        break;
                    }
                }
            }
        }

        if (is_final_code_found) {
            int path_length = 0;
            int code = final_code;
    
            while (code != initial_code) {
                code = parents[code];
                path_length++;
            }
    
            cout << "Case " << test << ": " << path_length << endl;
        } else {
            cout << "Case " << test << ": " << "Permanently Locked" << endl;
        }

        test++;
    }

    return 0;
}