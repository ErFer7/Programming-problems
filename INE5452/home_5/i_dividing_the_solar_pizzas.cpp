#include <algorithm>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int pizza_count;

    cin >> pizza_count;

    int flavors[pizza_count * 2];

    for (int i = 0; i < pizza_count * 2; i++) {
        cin >> flavors[i];
    }

    std::sort(flavors, flavors + pizza_count * 2);

    int min_price = 0;

    for (int i = 0; i < pizza_count * 2; i += 2) {
        if (flavors[i] >= flavors[i + 1]) {
            min_price += flavors[i];
        } else {
            min_price += flavors[i + 1];
        }
    }

    cout << min_price << endl;

    return 0;
}