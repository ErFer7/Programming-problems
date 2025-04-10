#include <iostream>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;

int main() {
    while (true) {
        int n, distance, rate;

        cin >> n >> distance >> rate;

        if (n == 0) {
            break;
        }

        int morning_routes[n];
        int evening_routes[n];

        for (int i = 0; i < n; i++) {
            cin >> morning_routes[i];
        }

        for (int i = 0; i < n; i++) {
            cin >> evening_routes[i];
        }

        std::sort(morning_routes, morning_routes + n);
        std::sort(
            evening_routes, 
            evening_routes + n,
            [](const int a, const int b) { return a > b; }
        );

        int overtime = 0;

        for (int i = 0; i < n; i++) {
            int length = morning_routes[i] + evening_routes[i];

            if (length > distance) {
                overtime += rate * (length - distance);
            }
        }

        cout << overtime << endl;
    }

    return 0;
}