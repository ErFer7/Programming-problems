#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

int depth_first_search_size(vector<vector<int>> &graph,
                            vector<int> &subtree_size, vector<bool> &visited,
                            int node) {
  visited[node] = true;
  subtree_size[node] = 1;

  for (int neighbor : graph[node]) {
    if (!visited[neighbor]) {
      subtree_size[node] +=
          depth_first_search_size(graph, subtree_size, visited, neighbor);
    }
  }

  return subtree_size[node];
}

void get_centroid(vector<vector<int>> &graph, vector<int> &subtree_size,
                  vector<bool> &visited, int node, int n, int &result) {
  visited[node] = true;
  bool is_centroid = true;

  for (int neighbor : graph[node]) {
    if (!visited[neighbor]) {
      int neighbor_size = subtree_size[neighbor];

      if (neighbor_size > n / 2) {
        is_centroid = false;
        get_centroid(graph, subtree_size, visited, neighbor, n, result);
        break;
      }
    }
  }

  int parent_size = n - subtree_size[node];
  if (parent_size > n / 2) {
    is_centroid = false;
  }

  if (is_centroid && result == -1) {
    result = node;
  }
}

int main() {
  int node;
  cin >> node;

  if (node == 1) {
    cout << 1 << endl;
    return 0;
  }

  vector<vector<int>> graph(node + 1);

  for (int i = 0; i < node - 1; i++) {
    int a, b;
    cin >> a >> b;
    graph[a].push_back(b);
    graph[b].push_back(a);
  }

  vector<int> subtree_size(node + 1, 0);
  vector<bool> visited(node + 1, false);
  depth_first_search_size(graph, subtree_size, visited, 1);

  visited.assign(node + 1, false);
  int centroid = -1;
  get_centroid(graph, subtree_size, visited, 1, node, centroid);

  cout << centroid << endl;

  return 0;
}
