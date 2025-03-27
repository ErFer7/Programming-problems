#include <iostream>
#include <ostream>
#include <iomanip>

using std::cin;
using std::cout;
using std::endl;

int digits2int(int digits[5]) {
    int result = 0;
    int multiplier = 1;

    for (int i = 4; i >= 0; i--) {
        result += digits[i] * multiplier;
        multiplier *= 10;
    }

    return result;
}

int main() {
    int number;
    bool not_first = false;

    while (true) {
        cin >> number;

        if (number == 0) {
            break;
        }

        if (not_first) {
            cout << '\n';
        }

        not_first = true;

        bool has_result = false;

        for (int numerator = 1234; numerator < 100000; numerator++) {
            int denominator = numerator / number;

            if (denominator < 1234 || denominator * number != numerator) {
                continue;  // É float
            }

            bool digits[10] = {false};
            int divisor = 10000;
            bool invalid = false;

            int numerator_checked = numerator;
            int denominator_checked = denominator;

            for (int i = 0; i < 5; i++) {
                int numerator_digit = numerator_checked / divisor;
                int denominator_digit = denominator_checked / divisor;

                numerator_checked -= numerator_digit * divisor;
                denominator_checked -= denominator_digit * divisor;

                if (!digits[numerator_digit]) {
                    digits[numerator_digit] = true;
                } else {
                    invalid = true;
                    break;
                }

                if (!digits[denominator_digit]) {
                    digits[denominator_digit] = true;
                } else {
                    invalid = true;
                    break;
                }

                divisor /= 10;
            }

            if (invalid) {
                continue;
            }

            int result = numerator / denominator;

            if (result * denominator == numerator && result == number) {
                has_result = true;

                cout << std::setfill('0') << std::setw(5) << numerator << " / " << std::setfill('0') << std::setw(5) <<  denominator << " = " << number << endl;
            }
        }

        if (!has_result) {
            cout << "There are no solutions for " << number << '.' << endl;
        }
    }

    return 0;
}