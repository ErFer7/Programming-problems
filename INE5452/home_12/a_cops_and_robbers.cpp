#include <math.h>

#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>

const float EPSILON = 1e-9;

struct Point {
    int x;
    int y;

    bool operator<(const Point &point) const { return x < point.x || (x == point.x && y < point.y); }

    bool operator==(const Point &point) const { return x == point.x && y == point.y; }
};

int cross(const Point &origin, const Point &point_a, const Point &point_b) {
    return (point_a.x - origin.x) * (point_b.y - origin.y) - (point_a.y - origin.y) * (point_b.x - origin.x);
}

float distance(const Point &point_a, const Point &point_b) {
    return std::sqrt(
        static_cast<float>((point_b.x - point_a.x) * (point_b.x - point_a.x) + (point_b.y - point_a.y) * (point_b.y - point_a.y)));
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

bool is_point_inside_hull(Point point, const std::vector<Point> &hull) {
    if (hull.size() < 3) {
        return false;
    }

    int hull_size = hull.size();
    bool is_clockwise = cross(hull[0], hull[1], hull[2]) < 0;
    bool is_inside = true;

    for (int i = 0; i < hull_size; i++) {
        int next = (i + 1) % hull_size;

        if (point == hull[i] || point == hull[next]) {
            return true;
        }

        int cross_product = cross(hull[i], hull[next], point);

        if (cross_product != 0) {
            if (is_clockwise) {
                if (cross_product < 0) {
                    is_inside = true;
                } else {
                    return false;
                }
            } else {
                if (cross_product > 0) {
                    is_inside = true;
                } else {
                    return false;
                }
            }
        } else {
            if (std::abs(distance(point, hull[i]) + distance(point, hull[next]) - distance(hull[i], hull[next])) < EPSILON) {
                return true;
            } else {
                is_inside = false;
            }
        }
    }

    return is_inside;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int dataset = 1;

    while (true) {
        int cop_count, robber_count, citizen_count;
        std::cin >> cop_count >> robber_count >> citizen_count;

        if (cop_count == 0 && robber_count == 0 && citizen_count == 0) {
            break;
        }

        std::vector<Point> cops(cop_count);
        std::vector<Point> robbers(robber_count);
        std::vector<Point> citizens(citizen_count);

        for (int i = 0; i < cop_count; i++) {
            std::cin >> cops[i].x >> cops[i].y;
        }

        for (int i = 0; i < robber_count; i++) {
            std::cin >> robbers[i].x >> robbers[i].y;
        }

        for (int i = 0; i < citizen_count; i++) {
            std::cin >> citizens[i].x >> citizens[i].y;
        }

        std::vector<Point> cop_hull = create_convex_hull(cops);
        std::vector<Point> robber_hull = create_convex_hull(robbers);

        std::cout << "Data set " << dataset++ << ':' << std::endl;

        for (int i = 0; i < citizen_count; i++) {
            std::cout << "     Citizen at (" << citizens[i].x << ',' << citizens[i].y << ") is ";

            if (is_point_inside_hull(citizens[i], cop_hull)) {
                std::cout << "safe." << std::endl;
            } else if (is_point_inside_hull(citizens[i], robber_hull)) {
                std::cout << "robbed." << std::endl;
            } else {
                std::cout << "neither." << std::endl;
            }
        }

        std::cout << std::endl;
    }
}
