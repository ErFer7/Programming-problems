#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <unordered_map>

using std::cin;
using std::cout;
using std::endl;

bool visited[1000 * 1000 + 2];

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int height, width;
    cin >> height >> width;

    // T, B, R, L
    std::unordered_map<int, int[4]> graph;
    std::vector<std::string> lines;
    std::vector<int> empty_nodes;

    for (int i = 0; i < height; i++) {
        std::string line;
        cin >> line;

        lines.push_back(line);

        for (int j = 0; j < width; j++) {
            int node = i * width + j;

            for (int k = 0; k < 4; k++) {
                graph[node][k] = -1;
            }

            if (lines[i][j] == '#') {
                continue;
            }

            empty_nodes.push_back(node);

            if (i > 0 && lines[i - 1][j] != '#') {
                int top_node = (i - 1) * width + j;
                graph[top_node][1] = node;
                graph[node][0] = top_node;
            }

            if (j > 0 && lines[i][j - 1] != '#') {
                int left_node = i * width + j - 1;
                graph[left_node][2] = node;
                graph[node][3] = left_node;
            }

        }
    }

    int room_count = 0;

    for (auto node : empty_nodes) {
        if (!visited[node]) {
            room_count++;

            std::queue<int> search_queue;
            search_queue.push(node);
            visited[node] = true;

            while(!search_queue.empty()) {
                int current_node = search_queue.front();
                search_queue.pop();

                for (int i = 0; i < 4; i++) {
                    int neighbor_node = graph[current_node][i];
    
                    if (neighbor_node != -1 && !visited[neighbor_node]) {
                        search_queue.push(neighbor_node);
                        visited[neighbor_node] = true;
                    }
                }
            }
        }
    }

    cout << room_count << endl;

    return 0;
}