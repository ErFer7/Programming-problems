#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

const int MAX_NODES = 50;

int bfs(int n, int s, int t, int capacity[MAX_NODES][MAX_NODES], std::vector<int>& parent) {
    parent.assign(n, -1);
    parent[s] = -2;

    std::queue<std::pair<int, int>> q;
    q.push({s, 40000001});

    while (!q.empty()) {
        int u = q.front().first;
        int flow = q.front().second;
        q.pop();

        for (int v = 0; v < n; ++v) {
            if (parent[v] == -1 && capacity[u][v] > 0) {
                parent[v] = u;
                int new_flow = std::min(flow, capacity[u][v]);
                if (v == t) {
                    return new_flow;
                }
                q.push({v, new_flow});
            }
        }
    }
    return 0;
}

void max_flow(int n, int s, int t, int capacity[MAX_NODES][MAX_NODES]) {
    std::vector<int> parent(n);
    int new_flow;

    while ((new_flow = bfs(n, s, t, capacity, parent))) {
        int current = t;

        while (current != s) {
            int previous = parent[current];
            capacity[previous][current] -= new_flow;
            capacity[current][previous] += new_flow;
            current = previous;
        }
    }
}

void find_reachable_nodes(int n, int s, int capacity[MAX_NODES][MAX_NODES], std::vector<bool>& reachable) {
    reachable.assign(n, false);
    std::queue<int> q;

    q.push(s);
    reachable[s] = true;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v = 0; v < n; ++v) {
            if (!reachable[v] && capacity[u][v] > 0) {
                reachable[v] = true;
                q.push(v);
            }
        }
    }
}


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n, m;
    while (std::cin >> n >> m && (n != 0 || m != 0)) {
        int source = 0;
        int sink = 1;

        std::vector<std::pair<int, int>> original_connections;
        int capacity[MAX_NODES][MAX_NODES] = {0};

        for (int i = 0; i < m; ++i) {
            int u, v, cost;
            std::cin >> u >> v >> cost;

            u--;
            v--;

            original_connections.push_back({u, v});

            capacity[u][v] += cost;
            capacity[v][u] += cost;
        }

        max_flow(n, source, sink, capacity);

        std::vector<bool> reachable;
        find_reachable_nodes(n, source, capacity, reachable);

        for (const auto& conn : original_connections) {
            int u = conn.first;
            int v = conn.second;
            
            if (reachable[u] != reachable[v]) {
                std::cout << u + 1 << " " << v + 1 << std::endl;
            }
        }
        
        std::cout << std::endl;
    }

    return 0;
}
