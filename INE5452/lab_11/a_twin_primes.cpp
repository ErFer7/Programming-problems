#include <iostream>
#include <bitset>

const long long UPPER_BOUND = 20000010;

int main() {
    int twin_primes[100001][2];
    int current_index = 0;

    std::bitset<UPPER_BOUND> bitset;

    bitset.set();
    bitset[0] = 0;
    bitset[1] = 0;
    int last_prime = -1;

    for (long long i = 2; i < UPPER_BOUND + 1; i++) if (bitset[i]) {
        for (long long j = i * i; j <= UPPER_BOUND + 1; j += i) {
            bitset[j] = 0;
        }

        int prime = (int)i;

        if (prime - last_prime == 2) {
            twin_primes[current_index][0] = last_prime;
            twin_primes[current_index][1] = prime;

            current_index++;
        }

        last_prime = prime;
    }

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    while (true) {
        int index;

        if (std::cin >> index) {
            std::cout << '(' << twin_primes[index - 1][0] << ", " << twin_primes[index - 1][1] << ')' << std::endl;
        } else {
            break;
        }
    }

    return 0;
}