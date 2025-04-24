#include <climits>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

struct Calls {
    unsigned long long cache_value;
    unsigned long long call_count;
};

Calls cache[62][61];
unsigned long long count;

unsigned long long trib(int n, unsigned int back) {
    count++;

    if (n <= 0) {
        return 0;
    }

    if (n == 1) {
        return 1;
    }

    if (cache[n][back].cache_value != ULLONG_MAX) {
        count += cache[n][back].call_count;
        return cache[n][back].cache_value;
    }

    unsigned long long sum = 0;
    unsigned long long internal_count_before = count;

    for (int i = 1; i <= back; i++) {
        sum += trib(n - i, back);
    }

    cache[n][back].cache_value = sum;
    cache[n][back].call_count = count - internal_count_before;

    return sum;
}

int main(void) {
    int test = 0;

    for (int i = 0; i < 62; i++) {
        for (int j = 0; j < 61; j++) {
            cache[i][j] = Calls{ULLONG_MAX, 0};
        }
    }

    while (true) {
        int n, back;
        cin >> n >> back;

        if (n >= 61) {
            break;
        }

        count = 0;
        trib(n, back);

        cout << "Case " << ++test << ": " << count << endl;
    }

    return 0;
}
