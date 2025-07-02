#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

const double EPSILON = 1e-9;

struct Point {
    double x;
    double y;

    bool operator==(const Point &other) const { return std::fabs(x - other.x) < EPSILON && std::fabs(y - other.y) < EPSILON; }
};

double cross(Point origin, Point point_a, Point point_b) {
    return (point_a.x - origin.x) * (point_b.y - origin.y) - (point_a.y - origin.y) * (point_b.x - origin.x);
}

std::vector<Point> cut_polygon(const std::vector<Point> &polygon, Point line_a, Point line_b) {
    std::vector<Point> resulting_polygon;

    for (size_t i = 0; i < polygon.size(); ++i) {
        Point current_point = polygon[i];
        Point next_point = polygon[(i + 1) % polygon.size()];

        double cut_a = cross(line_a, line_b, current_point);
        double cut_b = cross(line_a, line_b, next_point);

        bool is_current_inside = cut_a >= -EPSILON;
        bool is_next_inside = cut_b >= -EPSILON;

        if (is_current_inside) {
            resulting_polygon.push_back(current_point);
        }

        if (is_current_inside != is_next_inside) {
            double t = cut_a / (cut_a - cut_b);
            Point intersection = {current_point.x + t * (next_point.x - current_point.x),
                                  current_point.y + t * (next_point.y - current_point.y)};

            resulting_polygon.push_back(intersection);
        }
    }

    return resulting_polygon;
}

bool is_point_inside_polygon(Point p, const std::vector<Point> &polygon) {
    if (polygon.size() < 3) {
        return false;
    }

    int winding_number = 0;

    for (size_t i = 0; i < polygon.size(); ++i) {
        Point point_a = polygon[i];
        Point point_b = polygon[(i + 1) % polygon.size()];

        if (point_a.y <= p.y) {
            if (point_b.y > p.y && cross(point_a, point_b, p) > EPSILON) {
                winding_number++;
            }
        } else {
            if (point_b.y <= p.y && cross(point_a, point_b, p) < -EPSILON) {
                winding_number--;
            }
        }
    }

    return winding_number != 0;
}

double polygon_area(const std::vector<Point> &polygon) {
    double area = 0.0;

    for (size_t i = 0; i < polygon.size(); ++i) {
        Point point_a = polygon[i];
        Point point_b = polygon[(i + 1) % polygon.size()];

        area += (point_a.x * point_b.y - point_b.x * point_a.y);
    }

    return std::fabs(area) / 2.0;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout << std::fixed << std::setprecision(3);

    int line_count, width, height, fountain_x, fountain_y;
    int case_num = 1;

    while (std::cin >> line_count >> width >> height >> fountain_x >> fountain_y) {
        std::vector<std::pair<Point, Point>> lines(line_count);

        for (int i = 0; i < line_count; ++i) {
            double x1, y1, x2, y2;
            std::cin >> x1 >> y1 >> x2 >> y2;

            lines[i] = {{x1, y1}, {x2, y2}};
        }

        std::vector<Point> current_polygon(4);

        double width_double = static_cast<double>(width);
        double height_double = static_cast<double>(height);
        double fountain_x_double = static_cast<double>(fountain_x);
        double fountain_y_double = static_cast<double>(fountain_y);

        current_polygon[0] = {0.0, 0.0};
        current_polygon[1] = {width_double, 0.0};
        current_polygon[2] = {width_double, height_double};
        current_polygon[3] = {0.0, height_double};

        Point fountain = {fountain_x_double, fountain_y_double};

        for (const auto &line : lines) {
            std::vector<Point> polygon_left = cut_polygon(current_polygon, line.first, line.second);

            if (is_point_inside_polygon(fountain, polygon_left)) {
                current_polygon = polygon_left;
            } else {
                current_polygon = cut_polygon(current_polygon, line.second, line.first);
            }
        }

        std::cout << "Case #" << case_num++ << ": " << polygon_area(current_polygon) << std::endl;
    }

    return 0;
}
