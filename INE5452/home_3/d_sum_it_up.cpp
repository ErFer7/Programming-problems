#include <cstddef>
#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int target_number, number_count;

    while (true) {
        cin >> target_number >> number_count;

        if (number_count == 0) {
            break;
        }

        int numbers[number_count];

        for (int i = number_count - 1; i >= 0; i--) {
            cin >> numbers[i];
        }

        std::vector<unsigned int> solutions;
        solutions.reserve(1 << number_count);

        for (unsigned int bits = 0; bits < 1 << number_count; bits++) {
            int sum = 0;
            bool is_valid = true;

            for (int i = 0; i < number_count; i++) {
                if (bits & (1 << i)) {
                    if (numbers[i] > target_number) {
                        bits += 1 << number_count;
                        is_valid = false;
                        break;
                    }

                    sum += numbers[i];
                }
            }

            if (is_valid && sum == target_number) {
                solutions.emplace_back(bits);
            }
        }

        cout << "Sums of " << target_number << ":" << endl;

        if (solutions.empty()) {
            cout << "NONE" << endl;
        }

        std::vector<std::vector<int>> previous_solutions;
        std::vector<int> current_solution;

        current_solution.reserve(number_count);

        for (int i = solutions.size() - 1; i >= 0; i--) {
            for (int j = 0; j < number_count; j++) {
                if (solutions[i] & (1 << j)) {
                    current_solution.emplace_back(numbers[j]);
                }
            }

            bool is_duplicate = false;

            for (int j = 0; j < previous_solutions.size(); j++) {
                if (current_solution == previous_solutions[j]) {
                    is_duplicate = true;
                    current_solution.clear();
                    break;
                }
            }

            if (is_duplicate) {
                continue;
            }

            size_t solution_size = current_solution.size();

            for (int j = solution_size - 1; j >= 0; j--) {
                if (j == solution_size - 1) {
                    cout << current_solution[j];
                } else {
                    cout << "+" << current_solution[j];
                }
            }

            cout << endl;

            previous_solutions.emplace_back(current_solution);
            current_solution.clear();
            current_solution.reserve(number_count);
        }
    }

    return 0;
}