#include <iostream>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;

struct Task {
    long long duration;
    long long deadline;
};

int main() {
    int task_count;

    cin >> task_count;

    Task tasks[task_count];

    for (int i = 0; i < task_count; i++) {
        int duration, deadline;

        cin >> duration >> deadline;

        tasks[i] = Task{duration, deadline};
    }

    std::sort(tasks, tasks + task_count, [](Task const &a, Task const &b) {
        if (a.duration != b.duration) {
            return a.duration < b.duration;
        }

        return a.deadline < b.deadline;
    });

    long long reward = 0;
    long long time = 0;

    for (int i = 0; i < task_count; i++) {
        time += tasks[i].duration;
        reward += tasks[i].deadline - time;
    }

    cout << reward << endl;

    return 0;
}