#include <cmath>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

double function(double x, double p, double q, double r, double s, double t, double u) {
    return p * std::exp(-x) +
           q * std::sin(x) +
           r * std::cos(x) +
           s * std::tan(x) +
           t * std::pow(x, 2) +
           u;
}

int main() {
    while (true) {
        double p, q, r, s, t, u;

        if (!(cin >> p)) {
            break;
        }

        cin >> q;
        cin >> r;
        cin >> s;
        cin >> t;
        cin >> u;

        double lower = 0.0;
        double upper = 1.0;

        double x;
        double result;

        do {
            x = (upper + lower) / 2.0;

            result = function(x, p, q, r, s, t, u);
            double result_lower = function(lower, p, q, r, s, t, u);

            if (result_lower * result <= 0.0) {
                upper = x;
            } else {
                lower = x;
            }
        } while (std::fabs(upper - lower) > 0.000000001);

        if (std::fabs(result) < 0.00001) {
            printf("%.04f\n", x);
        } else {
            cout << "No solution" << endl;
        }
    }
}