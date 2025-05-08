#include <iostream>
#include <set>
#include <utility>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

int node_colors[200001];
std::vector<int> tree[200001];
int node_distinct_color_count[200001];
std::set<int> node_distinct_colors[200001];

void count_distinct_colors(int node, int parent) {
    for (int subnode : tree[node]) {
        if (subnode != parent) {
            count_distinct_colors(subnode, node);

            if (node_distinct_colors[subnode].size() > node_distinct_colors[node].size()) {
                std::swap(node_distinct_colors[node], node_distinct_colors[subnode]);
            }

            node_distinct_colors[node].merge(node_distinct_colors[subnode]);
        }
    }

    node_distinct_color_count[node] = node_distinct_colors[node].size();
}

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int node_count;
    cin >> node_count;

    for (int i = 0; i < node_count; i++) {
        int color;
        cin >> color;

        node_colors[i] = color;
        node_distinct_colors[i].insert(color);
    }

    for (int i = 0; i < node_count - 1; i++) {
        int node_a, node_b;
        cin >> node_a >> node_b;

        tree[node_a - 1].push_back(node_b - 1);
        tree[node_b - 1].push_back(node_a - 1);
    }

    count_distinct_colors(0, -1);

    for (int i = 0; i < node_count; i++) {
        cout << node_distinct_color_count[i] << ' ';
    }

    cout << endl;

    return 0;
}