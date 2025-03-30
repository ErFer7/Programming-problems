#include <algorithm>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

struct Rule {
    int teenager_a;
    int teenager_b;
    int distance;
};

int main() {
    int teenager_count, rule_count;

    while (true) {
        cin >> teenager_count >> rule_count;

        if (teenager_count == 0 && rule_count == 0) {
            break;
        }

        Rule rules[rule_count];

        for (int i = 0; i < rule_count; i++) {
            int teenager_a, teenager_b, distance;
            cin >> teenager_a >> teenager_b >> distance;

            rules[i] = Rule{teenager_a, teenager_b, distance};
        }

        int teenagers[teenager_count];

        for (int i = 0; i < teenager_count; i++) {
            teenagers[i] = i;
        }

        int possibilities = 0;

        do {
            bool valid = true;

            for (int i = 0; i < rule_count; i++) {
                Rule rule = rules[i];

                int position_a, position_b, distance;

                position_a = -1;
                position_b = -1;

                for (int j = 0; j < teenager_count; j++) {
                    if (teenagers[j] == rule.teenager_a) {
                        position_a = j;
                    } else if (teenagers[j] == rule.teenager_b) {
                        position_b = j;
                    }

                    if (position_a > 0 && position_b > 0) {
                        break;
                    }
                }

                distance = position_a > position_b ? position_a - position_b : position_b - position_a;

                if (!(rule.distance >= 0 && distance <= rule.distance || rule.distance < 0 && distance >= -rule.distance)) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                possibilities++;
            }
        } while (std::next_permutation(teenagers, teenagers + teenager_count));

        cout << possibilities << endl;
    }

    return 0;
}