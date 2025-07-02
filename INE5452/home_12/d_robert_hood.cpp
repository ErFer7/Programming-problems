#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

struct Point {
    int x;
    int y;

    bool operator<(const Point &point) const { return x < point.x || (x == point.x && y < point.y); }

    bool operator==(const Point &point) const { return x == point.x && y == point.y; }
};

int cross(const Point &origin, const Point &point_a, const Point &point_b) {
    return (point_a.x - origin.x) * (point_b.y - origin.y) - (point_a.y - origin.y) * (point_b.x - origin.x);
}

double distance(const Point &point_a, const Point &point_b) {
    return std::sqrt(
        static_cast<double>((point_b.x - point_a.x) * (point_b.x - point_a.x) + (point_b.y - point_a.y) * (point_b.y - point_a.y)));
}

std::vector<Point> create_convex_hull(std::vector<Point> &points) {
    int point_count = points.size();

    if (point_count <= 3) {
        return points;
    }

    std::vector<Point> hull(2 * point_count);
    std::sort(points.begin(), points.end());

    int k = 0;

    for (int i = 0; i < point_count; i++) {
        while (k >= 2 && cross(hull[k - 2], hull[k - 1], points[i]) <= 0) {
            k--;
        }

        hull[k++] = points[i];
    }

    int t = k + 1;

    for (int i = point_count - 1; i > 0; i--) {
        while (k >= t && cross(hull[k - 2], hull[k - 1], points[i - 1]) <= 0) {
            k--;
        }

        hull[k++] = points[i - 1];
    }

    hull.resize(k - 1);

    return hull;
}

double triangle_area(const Point &a, const Point &b, const Point &c) { return std::abs(cross(a, b, c)) / 2.0; }

double farthest_pair_distance(const std::vector<Point> &hull) {
    int size = hull.size();

    if (size == 2) {
        return distance(hull[0], hull[1]);
    }

    double farthest_distance = 0.0;

    int q = 1;
    while (q < size && triangle_area(hull[0], hull[1], hull[q]) < triangle_area(hull[0], hull[1], hull[(q + 1) % size])) {
        q++;
    }

    for (int p = 0; p < size; p++) {
        farthest_distance = std::max(farthest_distance, distance(hull[p], hull[q % size]));

        while (triangle_area(hull[p], hull[(p + 1) % size], hull[q % size]) <
               triangle_area(hull[p], hull[(p + 1) % size], hull[(q + 1) % size])) {
            q = (q + 1) % size;

            farthest_distance = std::max(farthest_distance, distance(hull[p], hull[q]));
        }
    }

    return farthest_distance;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout << std::fixed << std::setprecision(8);

    int arrow_count;
    std::cin >> arrow_count;

    std::vector<Point> points(arrow_count);

    for (int i = 0; i < arrow_count; i++) {
        std::cin >> points[i].x >> points[i].y;
    }

    std::vector<Point> convex_hull = create_convex_hull(points);

    double farthest_distance = farthest_pair_distance(convex_hull);

    std::cout << farthest_distance << std::endl;

    return 0;
}
