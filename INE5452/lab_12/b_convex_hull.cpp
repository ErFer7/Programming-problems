#include <algorithm>
#include <iostream>

struct Point {
    int x;
    int y;

    bool operator <(const Point &point) const {
        return x < point.x || (x == point.x && y < point.y);
    }

    bool operator ==(const Point &point) const {
        return x == point.x && y == point.y;
    }
};

int cross(const Point &origin, const Point &point_a, const Point &point_b) {
    return (point_a.x - origin.x) * (point_b.y - origin.y) - (point_a.y - origin.y) * (point_b.x - origin.x);
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    while (true) {
        int point_count;
        std::cin >> point_count;

        if (point_count == 0) {
            break;
        }

        Point points[10000]; 
        
        for (int i = 0; i < point_count; i++) {
            int x;
            int y;
            std::cin >> x >> y;
            points[i] = Point{x, y};
        }
        
        if (point_count == 1) {
            std::cout << 1 << std::endl;
            std::cout << points[0].x << ' ' << points[0].y << std::endl;
            continue;
        }

        bool all_identical = true;

        for (int i = 1; i < point_count; ++i) {
            if (!(points[i] == points[0])) {
                all_identical = false;
                break;
            }
        }

        if (all_identical) {
            std::cout << 1 << std::endl;
            std::cout << points[0].x << ' ' << points[0].y << std::endl;
            continue;
        }

        Point convex_hull[10000];

        std::sort(points, points + point_count);

        int k = 0;

        for (int i = 0; i < point_count; i++) {
            while (k >= 2 && cross(convex_hull[k - 2], convex_hull[k - 1], points[i]) <= 0) {
                k--;
            }

            convex_hull[k++] = points[i];
        }

        int t = k + 1; 
        for (int i = point_count - 1; i > 0; i--) {
            while (k >= t && cross(convex_hull[k - 2], convex_hull[k - 1], points[i - 1]) <= 0) {
                k--;
            }

            convex_hull[k++] = points[i - 1];
        }

        std::cout << k - 1 << std::endl; 

        for (int i = 0; i < k - 1; i++) {
            std::cout << convex_hull[i].x << ' ' << convex_hull[i].y << std::endl;
        }
    }
}