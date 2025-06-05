#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

const int MAX_NODES = 100;

int bfs(int n, int s, int t, int capacity[MAX_NODES][MAX_NODES], std::vector<int>& parent) {
    parent.assign(n, -1);
    parent[s] = -2;

    std::queue<std::pair<int, int>> q;
    q.push({s, 1001});

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

int max_flow(int n, int s, int t, int capacity[MAX_NODES][MAX_NODES]) {
    int flow = 0;
    std::vector<int> parent(n);
    int new_flow;

    while ((new_flow = bfs(n, s, t, capacity, parent))) {
        flow += new_flow;
        int current = t;
        while (current != s) {
            int previous = parent[current];
            capacity[previous][current] -= new_flow;
            capacity[current][previous] += new_flow;
            current = previous;
        }
    }

    return flow;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int network_num = 1;
    int n;

    while (std::cin >> n && n != 0) {
        int s, t, c;
        std::cin >> s >> t >> c;

        s--;
        t--;

        int capacity[MAX_NODES][MAX_NODES] = {0};

        for (int i = 0; i < c; ++i) {
            int u, v, w;
            std::cin >> u >> v >> w;
            u--;
            v--;
            
            capacity[u][v] += w;
            capacity[v][u] += w;
        }

        int total_bandwidth = max_flow(n, s, t, capacity);

        std::cout << "Network " << network_num << std::endl;
        std::cout << "The bandwidth is " << total_bandwidth << "." << std::endl;
        std::cout << std::endl;

        network_num++;
    }

    return 0;
}
