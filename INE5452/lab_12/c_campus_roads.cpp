#include <math.h>

#include <iomanip>
#include <iostream>

int main() {
    std::cout << std::fixed << std::setprecision(2);

    int road_count;
    std::cin >> road_count;

    for (int i = 0; i < road_count; i++) {
        int point_count, tree_count;
        std::cin >> point_count >> tree_count;

        double points[point_count][2];
        double distances[point_count - 1];
        double total_distance = 0.0f;

        for (int j = 0; j < point_count; j++) {
            std::cin >> points[j][0] >> points[j][1];

            if (tree_count > 2 && j > 0) {
                double diff_x = points[j][0] - points[j - 1][0];
                double diff_y = points[j][1] - points[j - 1][1];

                distances[j - 1] = std::sqrt(diff_x * diff_x + diff_y * diff_y);
                total_distance += distances[j - 1];
            }
        }

        std::cout << "Road #" << i + 1 << ':' << std::endl;

        double optimal_distance = total_distance / (static_cast<double>(tree_count) - 1.0f);
        double current_distance = 0.0f;
        int current_road = 0;
        double road_start_distance = 0.0f;

        for (int i = 0; i < tree_count; i++) {
            double target_distance = i * optimal_distance;
            double x, y;

            if (i == 0) {
                x = points[0][0];
                y = points[0][1];
            } else if (i == tree_count - 1) {
                x = points[point_count - 1][0];
                y = points[point_count - 1][1];
            } else {
                while (current_road < point_count - 1 && road_start_distance + distances[current_road] < target_distance) {
                    road_start_distance += distances[current_road];
                    current_road++;
                }

                double distance_along_road = target_distance - road_start_distance;
                double ratio = distance_along_road / distances[current_road];

                x = points[current_road][0] + ratio * (points[current_road + 1][0] - points[current_road][0]);
                y = points[current_road][1] + ratio * (points[current_road + 1][1] - points[current_road][1]);
            }

            std::cout << x << ' ' << y << std::endl;
        }

        std::cout << std::endl;
    }
}