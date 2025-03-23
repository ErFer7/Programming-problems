#include <algorithm>
#include <iostream>
#include <vector>

struct TimeEvent {
  int time;
  int type; // 0 para o início, 1 para o fim

  TimeEvent(int t, int ty) : time(t), type(ty) {}

  bool operator<(const TimeEvent &other) const {
    if (time == other.time) {
      return type > other.type;
    }
    return time < other.time;
  }
};

int main() {
  int one_time_tasks, repeating_tasks;

  while (true) {
    std::cin >> one_time_tasks >> repeating_tasks;

    if (one_time_tasks == 0 && repeating_tasks == 0) {
      break;
    }

    std::vector<TimeEvent> times;
    times.reserve((one_time_tasks + repeating_tasks) * 2);

    for (int i = 0; i < one_time_tasks; i++) {
      int start, end;

      std::cin >> start >> end;

      times.emplace_back(start, 0);
      times.emplace_back(end, 1);
    }

    for (int i = 0; i < repeating_tasks; i++) {
      int start, end, interval;
      std::cin >> start >> end >> interval;

      while (start < 1000000) {
        times.emplace_back(start, 0);
        times.emplace_back(end, 1);

        start += interval;
        end += interval;
      }
    }

    std::sort(times.begin(), times.end());

    bool in_task = false;
    bool conflict = false;

    for (const auto &time : times) {
      if (time.type == 0) {
        if (in_task) {
          conflict = true;
          break;
        }
        in_task = true;
      } else {
        in_task = false;
      }
    }

    std::cout << (conflict ? "CONFLICT" : "NO CONFLICT") << std::endl;
  }

  return 0;
}