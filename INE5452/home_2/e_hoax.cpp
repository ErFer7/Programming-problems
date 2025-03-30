#include <iostream>
#include <set>

int main() {
    int days;

    while (true) {
        std::cin >> days;

        if (days == 0) {
            break;
        }

        std::multiset<int> urn;
        long paid_value = 0;

        for (int i = 0; i < days; i++) {
            int num_bills;
            std::cin >> num_bills;

            if (num_bills > 0) {
                for (int j = 0; j < num_bills; j++) {
                    int bill;
                    std::cin >> bill;
                    urn.insert(bill);
                }
            }

            if (!urn.empty()) {
                int lowest_bill = *urn.begin();
                int highest_bill = *urn.rbegin();

                urn.erase(urn.begin());
                urn.erase(--urn.end());

                paid_value += highest_bill - lowest_bill;
            }
        }

        std::cout << paid_value << std::endl;
    }

    return 0;
}
