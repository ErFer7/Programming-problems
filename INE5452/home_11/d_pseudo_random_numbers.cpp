#include <iostream>

int z, i, m;

int rng(int l) { return (z * l + i) % m; }

int floyd_cycle_finding(int x0) {
    int tortoise = rng(x0), hare = rng(rng(x0));

    while (tortoise != hare) {
        tortoise = rng(tortoise);
        hare = rng(rng(hare));
    }

    hare = x0;

    while (tortoise != hare) {
        tortoise = rng(tortoise);
        hare = rng(hare);
    }

    int lambda = 1;
    hare = rng(tortoise);

    while (tortoise != hare) {
        hare = rng(hare);
        lambda++;
    }

    return lambda;
}

int main() {
    int test = 1;

    while (true) {
        int l;
        std::cin >> z >> i >> m >> l;

        if (z == 0 && i == 0 && m == 0 && l == 0) {
            break;
        }

        std::cout << "Case " << test++ << ": " << floyd_cycle_finding(l) << std::endl;
    }

    return 0;
}
