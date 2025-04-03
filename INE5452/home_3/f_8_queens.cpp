#include <cmath>
#include <cstdlib>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

void calculate_minimum_moves(int &minimum_moves, int move_count, int queens_positions[8], int queen_to_move) {
    if (queen_to_move == 8) {
        if (move_count < minimum_moves) {
            minimum_moves = move_count;
        }

        return;
    }

    int original_position = queens_positions[queen_to_move];

    for (int i = 0; i < 8; i++) {
        int new_queens_positions[8];

        for (int j = 0; j < 8; j++) {
            new_queens_positions[j] = queens_positions[j];
        }

        new_queens_positions[queen_to_move] = i;

        bool valid = true;

        for (int j = 0; j < queen_to_move; j++) {
            if (new_queens_positions[j] == i) {
                valid = false;
                break;
            }

            if (abs(i - new_queens_positions[j]) == abs(queen_to_move - j)) {
                valid = false;
                break;
            }
        }

        if (valid) {
            int new_move_count = i != original_position ? move_count + 1 : move_count;
            calculate_minimum_moves(minimum_moves, new_move_count, new_queens_positions, queen_to_move + 1);
        }
    }
}

int main() {
    int test = 1;

    while (true) {
        int queens_positions[8];
        int minimum_moves = 8;

        for (int i = 0; i < 8; i++) {
            int queen_position;

            if (cin >> queen_position) {
                queens_positions[i] = queen_position - 1;
            } else {
                return 0;
            }
        }

        calculate_minimum_moves(minimum_moves, 0, queens_positions, 0);

        cout << "Case " << test << ": " << minimum_moves << endl;
        test++;
    }
}