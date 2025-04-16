#include <algorithm>
#include <iostream>
#include <queue>

using std::cin;
using std::cout;
using std::endl;

struct Cow {
    int milk_gallons;
    int deadline;

    bool operator<(Cow const &other) const { return milk_gallons < other.milk_gallons; }
};

int main() {
    int cow_count;

    cin >> cow_count;

    Cow cows[cow_count];

    for (int i = 0; i < cow_count; i++) {
        int milk_gallons, deadline;

        cin >> milk_gallons >> deadline;

        cows[i] = Cow{milk_gallons, deadline};
    }

    std::sort(cows, cows + cow_count, [](Cow const &a, Cow const &b) {
        if (a.deadline == b.deadline) {
            return a.milk_gallons < b.milk_gallons;
        }

        return a.deadline < b.deadline;
    });

    std::priority_queue<Cow> cows_queue;
    int total_milk_gallons = 0;
    int time = cows[cow_count - 1].deadline - 1;
    int next_i = cow_count - 1;
    int i = cow_count - 1;

    while (time >= 0) {
        if (i >= 0) {
            for (int j = i; j >= 0; j--) {
                if (cows[j].deadline > time) {
                    next_i--;
                    cows_queue.push(cows[j]);
                } else {
                    break;
                }
            }
        }

        if (!cows_queue.empty()) {
            Cow cow = cows_queue.top();
            cows_queue.pop();
            total_milk_gallons += cow.milk_gallons;
        }

        time--;
        i = next_i;
    }

    cout << total_milk_gallons << endl;

    return 0;
}