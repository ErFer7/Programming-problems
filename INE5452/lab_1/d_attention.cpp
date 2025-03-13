#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
    int num_directors;
    int time;

    cin >> num_directors;
    cin >> time;

    cout << (time - num_directors + 1) / num_directors << endl;

    return 0;
}