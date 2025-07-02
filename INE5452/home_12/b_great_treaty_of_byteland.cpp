#include <math.h>

#include <algorithm>
#include <iostream>
#include <vector>

struct UniquePoint {
    int id;
    int x;
    int y;

    bool operator<(const UniquePoint &point) const { return x < point.x || (x == point.x && y < point.y); }

    bool operator==(const UniquePoint &point) const { return x == point.x && y == point.y; }
};

int cross(const UniquePoint &origin, const UniquePoint &point_a, const UniquePoint &point_b) {
    return (point_a.x - origin.x) * (point_b.y - origin.y) - (point_a.y - origin.y) * (point_b.x - origin.x);
}

std::vector<UniquePoint> create_convex_hull(std::vector<UniquePoint> &points) {
    int point_count = points.size();

    if (point_count <= 1) {
        return points;
    }

    std::sort(points.begin(), points.end());

    if (point_count == 2) {
        return points;
    }

    bool all_collinear = true;

    for (int i = 2; i < point_count; i++) {
        if (cross(points[0], points[1], points[i]) != 0) {
            all_collinear = false;
            break;
        }
    }

    if (all_collinear) {
        return points;
    }

    std::vector<UniquePoint> hull(2 * point_count);
    int k = 0;

    for (int i = 0; i < point_count; i++) {
        while (k >= 2 && cross(hull[k - 2], hull[k - 1], points[i]) < 0) {
            k--;
        }
        hull[k++] = points[i];
    }

    int t = k + 1;

    for (int i = point_count - 2; i >= 0; i--) {
        while (k >= t && cross(hull[k - 2], hull[k - 1], points[i]) < 0) {
            k--;
        }
        hull[k++] = points[i];
    }

    hull.resize(k - 1);

    return hull;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int kingdom_count;
    std::cin >> kingdom_count;

    std::vector<UniquePoint> capitals(kingdom_count);

    for (int i = 0; i < kingdom_count; i++) {
        capitals[i].id = i + 1;

        std::cin >> capitals[i].x >> capitals[i].y;
    }

    std::vector<UniquePoint> convex_hull = create_convex_hull(capitals);

    std::vector<int> infinite_kingdoms(convex_hull.size());

    for (int i = 0; i < convex_hull.size(); i++) {
        infinite_kingdoms[i] = convex_hull[i].id;
    }

    std::sort(infinite_kingdoms.begin(), infinite_kingdoms.end());

    for (int i = 0; i < infinite_kingdoms.size(); i++) {
        std::cout << infinite_kingdoms[i];

        if (i < infinite_kingdoms.size() - 1) {
            std::cout << ' ';
        }
    }

    std::cout << std::endl;
}
