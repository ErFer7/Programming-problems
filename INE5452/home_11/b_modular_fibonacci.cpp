#include <math.h>

#include <iostream>

void multiply_matrices(long long a[2][2], long long b[2][2], long long mod) {
    long long temp00 = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod;
    long long temp01 = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod;
    long long temp10 = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod;
    long long temp11 = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod;

    a[0][0] = temp00;
    a[0][1] = temp01;
    a[1][0] = temp10;
    a[1][1] = temp11;
}

long long modular_fibonacci(int n, int m) {
    if (n == 0) return 0;

    long long fib_matrix[2][2] = {{1, 1}, {1, 0}};
    long long result_matrix[2][2] = {{1, 0}, {0, 1}};
    long long mod = 1LL << m;

    while (n > 0) {
        if (n % 2 == 1) {
            multiply_matrices(result_matrix, fib_matrix, mod);
        }

        multiply_matrices(fib_matrix, fib_matrix, mod);
        n /= 2;
    }

    return result_matrix[0][1];
}

int main() {
    while (true) {
        int n, m;

        if (!(std::cin >> n >> m)) {
            break;
        }

        std::cout << modular_fibonacci(n, m) << std::endl;
    }

    return 0;
}