#include <math.h>

#include <iostream>

long long extended_euclid_gcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;

        return a;
    }

    long long x1, y1;
    long long gcd = extended_euclid_gcd(b, a % b, x1, y1);

    x = y1;
    y = x1 - (a / b) * y1;

    return gcd;
}

int main() {
    while (true) {
        long long marbles;
        std::cin >> marbles;

        if (marbles == 0) {
            break;
        }

        long long cost_1, capacity_1;
        long long cost_2, capacity_2;
        std::cin >> cost_1 >> capacity_1;
        std::cin >> cost_2 >> capacity_2;

        long long x, y;
        long long gcd = extended_euclid_gcd(capacity_1, capacity_2, x, y);

        if (marbles % gcd != 0) {
            std::cout << "failed" << std::endl;

            continue;
        }

        long long box_1_amount = x * (marbles / gcd);
        long long box_2_amount = y * (marbles / gcd);

        long long lower_bound = std::ceil(-static_cast<double>(box_1_amount * gcd) / capacity_2);
        long long upper_bound = std::floor(static_cast<double>(box_2_amount * gcd) / capacity_1);

        if (lower_bound > upper_bound) {
            std::cout << "failed" << std::endl;

            continue;
        }

        double slope = static_cast<double>(capacity_2 * cost_1 - capacity_1 * cost_2) / gcd;

        long long optimal_factor = slope > 0.0f ? lower_bound : upper_bound;

        long long optimal_box_1_amount = box_1_amount + optimal_factor * capacity_2 / gcd;
        long long optimal_box_2_amount = box_2_amount - optimal_factor * capacity_1 / gcd;

        std::cout << optimal_box_1_amount << " " << optimal_box_2_amount << std::endl;
    }

    return 0;
}
