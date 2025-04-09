#include <cmath>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

double powers[10];

void precompute_powers(double base, int max_exp) {
    powers[0] = 1.0;
    for (int i = 1; i < max_exp; i++) {
        powers[i] = powers[i - 1] * base;
    }
}

double function(double cash_flows[10], int cash_flow_count, double irr) {
    precompute_powers(1.0 + irr, cash_flow_count);

    double result = 0.0;
    for (int i = 0; i < cash_flow_count; i++) {
        result += cash_flows[i] / powers[i];
    }
    return result;
}

int main() {
    while (true) {
        int cash_flow_count;
        cin >> cash_flow_count;

        if (cash_flow_count == 0) break;

        cash_flow_count++;
        double cash_flows[10];

        for (int i = 0; i < cash_flow_count; i++) {
            cin >> cash_flows[i];
        }

        const int intervals = 1000;
        const double max_upper = 100.0;

        int root_count = 0;
        double valid_irr;

        double function_start = function(cash_flows, cash_flow_count, -0.99);
        double function_end = function(cash_flows, cash_flow_count, max_upper);

        if (function_start * function_end > 0) {
            cout << "No" << endl;
            continue;
        }

        for (int i = 0; i < intervals && root_count < 2; i++) {
            double lower = -0.99 + (max_upper / intervals) * i;
            double upper = -0.99 + (max_upper / intervals) * (i + 1);
            double result_lower = function(cash_flows, cash_flow_count, lower);

            if (std::fabs(result_lower) < 0.00001) {
                root_count++;
                valid_irr = lower;
                continue;
            }

            double result_upper = function(cash_flows, cash_flow_count, upper);
            if (result_lower * result_upper > 0) continue;

            for (int iter = 0; iter < 50; iter++) {
                double irr = (upper + lower) / 2.0;
                double result = function(cash_flows, cash_flow_count, irr);

                if (std::fabs(result) < 0.00001) {
                    root_count++;
                    valid_irr = irr;
                    break;
                }

                if (result * result_lower <= 0) {
                    upper = irr;
                } else {
                    lower = irr;
                    result_lower = result;
                }

                if (std::fabs(upper - lower) < 0.000000001) break;
            }
        }

        if (root_count > 1) {
            cout << "Too many" << endl;
        } else if (root_count == 1) {
            printf("%.02f\n", valid_irr);
        } else {
            cout << "No" << endl;
        }
    }
    return 0;
}