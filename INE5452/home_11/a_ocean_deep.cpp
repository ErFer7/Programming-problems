#include <cstdio>
#include <iostream>

const int MOD = 131071;

int main() {
    long long number = 0;

    while (true) {
        char digit = getchar();

        if (digit == EOF) {
            break;
        }

        if (digit == '#') {
            std::cout << (number == 0 ? "YES" : "NO") << std::endl;
            number = 0;

            continue;
        }

        if (digit == '0' || digit == '1') {
            int digit_value = digit - '0';
            number = ((number << 1) + digit_value) % MOD;
        }
    }

    return 0;
}
