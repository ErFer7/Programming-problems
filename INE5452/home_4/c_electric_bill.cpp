#include <cmath>
#include <cstdlib>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

long cost(long consumption) {
    if (consumption > 1000000) {
        return (consumption - 1000000) * 7 + 990000 * 5 + 9900 * 3 + 100 * 2;
    }

    if (consumption >= 10001) {
        return (consumption - 10000) * 5 + 9900 * 3 + 100 * 2;
    }

    if (consumption >= 101) {
        return (consumption - 100) * 3 + 100 * 2;
    }

    return consumption * 2;
}

long consumption(long cost) {
    if (cost > 4979900) {
        long base = (cost - 4979900) / 7 + 1000000;
        if ((cost - 4979900) % 7 != 0) base++;

        return base;
    }

    if (cost > 29900) {
        long base = (cost - 29900) / 5 + 10000;
        if ((cost - 29900) % 5 != 0) base++;

        return base;
    }

    if (cost > 200) {
        long base = (cost - 200) / 3 + 100;
        if ((cost - 200) % 3 != 0) base++;

        return base;
    }

    long base = cost / 2;
    if (cost % 2 != 0) base++;

    return base;
}

int main() {
    while (true) {
        long total_cost, difference_cost;

        cin >> total_cost >> difference_cost;

        if (total_cost == 0 && difference_cost == 0) {
            break;
        }

        long total_consumption = consumption(total_cost);

        long upper = total_consumption;
        long lower = 0;

        while (lower < upper) {
            long middle = (upper + lower) / 2;
            long possible_neighbor_consumption = total_consumption - middle;

            if (std::abs(cost(possible_neighbor_consumption) - cost(middle)) == difference_cost ) {
                cout << cost(middle) << endl;
                break;
            }

            if (std::abs(cost(possible_neighbor_consumption) - cost(middle)) > difference_cost) {
                lower = middle;
            } else {
                upper = middle;
            }
        }
    }

    return 0;
}