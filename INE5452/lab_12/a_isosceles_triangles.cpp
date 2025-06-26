#include <iostream>
#include <unordered_map>
#include <math.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    while (true) {
        int point_count;
        std::cin >> point_count;

        if (point_count == 0) {
            break;
        }

        int points[1000][2];
        
        for (int i = 0; i < point_count; i++) {
            std::cin >> points[i][0] >> points[i][1];
        }
        
        int triangle_count = 0;
        std::unordered_map<double, int> distance_count;

        for (int i = 0; i < point_count; i++) {
            distance_count.clear();
            distance_count.reserve(1000);

            long x = static_cast<long>(points[i][0]);
            long y = static_cast<long>(points[i][1]);

            for (int j = 0; j < point_count; j++) {
                long next_x = static_cast<long>(points[j][0]);
                long next_y = static_cast<long>(points[j][1]);

                double distance = std::sqrt((next_x - x) * (next_x - x) + (next_y - y) * (next_y - y));
                distance_count[distance]++;
            }

            for (auto [distance, count] : distance_count) {
                triangle_count += count * (count - 1) / 2;
            }
        }

        std::cout << triangle_count << std::endl;
    }
}