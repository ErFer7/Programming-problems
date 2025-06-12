#include <iostream>
#include <unordered_map>
#include <cmath>

bool m_divides_n(long long n, long long m) {
    if (m == 0) {
        return false;
    }

    if (m == 1) {
        return true;
    }

    std::unordered_map<long long, int> m_prime_factors;
    long long temp_m = m;

    for (long long i = 2; i * i <= temp_m; ++i) {
        if (temp_m % i == 0) {
            int count = 0;
            while (temp_m % i == 0) {
                count++;
                temp_m /= i;
            }
            m_prime_factors[i] = count;
        }
    }

    if (temp_m > 1) {
        m_prime_factors[temp_m] = 1;
    }

    for (auto const& [prime, exponent_in_m] : m_prime_factors) {
        int exponent_n_factorial = 0;
        long long prime_power = prime;

        while (prime_power <= n) {
            exponent_n_factorial += n / prime_power;
            
            if (prime_power > n / prime) {
                break;
            }
            prime_power *= prime;
        }

        if (exponent_n_factorial < exponent_in_m) {
            return false;
        }
    }

    return true;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    long long n, m;
    
    while (std::cin >> n >> m) {
        if (m_divides_n(n, m)) {
            std::cout << m << " divides " << n << "!" << std::endl;
        } else {
            std::cout << m << " does not divide " << n << "!" << std::endl;
        }
    }

    return 0;
}
