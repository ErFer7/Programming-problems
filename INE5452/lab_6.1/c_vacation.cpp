#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;

struct Activities {
    int swimming;
    int catch_bugs;
    int homework;
};

int main() {
    int day_count;
    cin >> day_count;

    Activities days[day_count];

    for (int i = 0; i < day_count; i++) {
        int swimming, catch_bugs, homework;
        cin >> swimming >> catch_bugs >> homework;

        days[i] = Activities{swimming, catch_bugs, homework};
    }

    Activities happiness[day_count];

    happiness[0] = days[0];

    for (int i = 1; i < day_count; i++) {
        int swimming_happiness = days[i].swimming + std::max(happiness[i - 1].catch_bugs, happiness[i - 1].homework);
        int catch_bug_happiness = days[i].catch_bugs + std::max(happiness[i - 1].swimming, happiness[i - 1].homework);
        int homework_happiness = days[i].homework + std::max(happiness[i - 1].swimming, happiness[i - 1].catch_bugs);

        happiness[i] = Activities{swimming_happiness, catch_bug_happiness, homework_happiness};
    }

    int total_max = std::max(happiness[day_count - 1].swimming, happiness[day_count - 1].catch_bugs);
    total_max = std::max(total_max, happiness[day_count - 1].homework);

    cout << total_max << endl;

    return 0;
}
