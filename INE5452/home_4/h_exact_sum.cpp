#include <algorithm>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int book_count;

    while (true) {
        if (!(cin >> book_count)) {
            break;
        }

        int prices[book_count];

        for (int i = 0; i < book_count; i++) {
            cin >> prices[i];
        }

        std::sort(prices, prices + book_count);

        int money;

        cin >> money;

        int first_book_price;
        int second_book_price;
        int min_difference = 1000001;

        for (int i = 0; i < book_count; i++) {
            if (prices[i] > money) {
                continue;
            }

            int complement = money - prices[i];

            if (std::binary_search(prices + i + 1, prices + book_count, complement)) {
                if (complement - prices[i] < min_difference) {
                    min_difference = complement - prices[i];
                    first_book_price = prices[i];
                    second_book_price = complement;
                }
            }
        }

        cout << "Peter should buy books whose prices are " << first_book_price << " and " << second_book_price << ".\n" << endl;
    }

    return 0;
}