#include <iostream>
#include <vector>
#include <queue>

using std::cin;
using std::cout;
using std::endl;

const int MAX_SIZE = 100000;

std::vector<int> graph[MAX_SIZE];
int parents[MAX_SIZE];
bool visited[MAX_SIZE] = {false};

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int node_count;
    int edge_count;
    cin >> node_count >> edge_count;

    for (int i = 0; i < edge_count; i++) {
        int a_node, b_node;
        cin >> a_node >> b_node;

        graph[a_node - 1].push_back(b_node - 1);
        graph[b_node - 1].push_back(a_node - 1);
    }

    int target_node = node_count - 1;
    std::queue<int> search_queue;
    bool has_found = false;

    search_queue.push(0);
    visited[0] = true;

    while (!search_queue.empty() && !has_found) {
        int current_node = search_queue.front();
        search_queue.pop();

        for (auto neighbor_node : graph[current_node]) {
            
            if (!visited[neighbor_node]) {
                search_queue.push(neighbor_node);
                visited[neighbor_node] = true;
                parents[neighbor_node] = current_node;

                if (neighbor_node == target_node) {
                    has_found = true;
                    break;
                }
            }
        }
    }

    if (has_found) {
        int count = 1;
        int node = target_node;
        std::vector<int> path;
        path.push_back(target_node);

        while (node > 0) {
            node = parents[node];
            count++;
            path.push_back(node);
        }

        cout << count << endl;

        for (int i = count - 1; i >= 0; i--) {
            cout << path[i] + 1 << (i > 0 ? ' ' : '\n');
        }
    } else {
        cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}