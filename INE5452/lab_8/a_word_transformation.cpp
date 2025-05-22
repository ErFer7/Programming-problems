#include <iostream>
#include <unordered_map>
#include <string>
#include <sstream>
#include <vector>
#include <queue>

using std::cin;
using std::cout;
using std::endl;

bool check_string_diff(std::string &str_a, std::string &str_b) {
    if (str_a.length() != str_b.length() || str_a == str_b) {
        return false;
    }

    bool has_single_difference = false;

    for (int i = 0; i < str_a.length(); i++) {
        if (str_a[i] != str_b[i]) {
            if (has_single_difference) {
                return false;
            } else {
                has_single_difference = true;
            }
        }
    }

    return has_single_difference;
}

int main() {
    int test_count;
    cin >> test_count;

    for (int i = 0; i < test_count; i++) {
        std::unordered_map<std::string, std::vector<std::string>> graph;

        while (true) {
            std::string word;
            cin >> word;

            if (word == "*") {
                break;
            }

            graph[word] = std::vector<std::string>();
        }

        for (auto vertex_pair : graph) {
            std::string word = vertex_pair.first;
            
            for (auto comparison_vertex_pair : graph) {
                std::string comparison_word = comparison_vertex_pair.first;

                if (check_string_diff(word, comparison_word)) {
                    graph[word].push_back(comparison_word);
                    graph[comparison_word].push_back(word);
                }
            }
        }

        std::string initial_word;
        std::string final_word;

        cin.ignore();

        while (true) {
            std::string line;
            std::getline(cin, line);

            if (line == "") {
                break;
            }

            std::stringstream stream(line);
            stream >> initial_word >> final_word;

            std::queue<std::string> queue;
            std::unordered_map<std::string, std::string> parents;
            std::unordered_map<std::string, bool> visited;
            bool is_final_word_found = false;

            queue.push(initial_word);
            visited[initial_word] = true;

            while (!queue.empty() && !is_final_word_found) {
                std::string vertex = queue.front();
                queue.pop();

                for (std::string neighbor : graph[vertex]) {
                    if (!visited[neighbor]) {
                        queue.push(neighbor);
                        parents[neighbor] = vertex;
                        visited[neighbor] = true;

                        if (neighbor == final_word) {
                            is_final_word_found = true;
                            break;
                        }
                    }
                }
            }

            int path_length = 0;
            std::string word = final_word;

            while (word != initial_word) {
                word = parents[word];
                path_length++;
            }

            cout << initial_word << ' ' << final_word << ' ' << path_length << endl;
        }

        if (i < test_count - 1) {
            cout << endl;
        }
    }

    return 0;
}