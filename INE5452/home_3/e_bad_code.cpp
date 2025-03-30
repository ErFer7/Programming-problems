#include <algorithm>
#include <iostream>
#include <ostream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

struct CodeLetter {
    std::string code;
    char letter;
};

void decode(const int &letter_count,
            const CodeLetter *code_letter_table,
            std::string remaining_code,
            std::string decoded_message,
            std::vector<std::string> &decoded_messages) {
    if (remaining_code.empty()) {
        decoded_messages.push_back(decoded_message);
        return;
    }

    for (int i = 0; i < letter_count; i++) {
        bool match = true;

        int remaining_code_index = 0;
        bool leading_zeroes = true;
        int zero_count = 0;

        for (int j = 0; j < code_letter_table[i].code.length(); j++) {
            char code_part;

            do {
                code_part = remaining_code[remaining_code_index];

                if (code_part == '0' && leading_zeroes) {
                    remaining_code_index++;
                    zero_count++;
                    continue;
                }

                leading_zeroes = false;
                break;
            } while (remaining_code_index < remaining_code.length());

            if (code_part == code_letter_table[i].code[j] && zero_count != remaining_code.length()) {
                remaining_code_index++;
            } else {
                match = false;
                break;
            }
        }

        if (match) {
            std::string new_decoded_message = decoded_message + code_letter_table[i].letter;
            std::string new_remaining_code = remaining_code.substr(code_letter_table[i].code.length() + zero_count);

            if (decoded_messages.size() < 100) {
                decode(letter_count, code_letter_table, new_remaining_code, new_decoded_message, decoded_messages);
            }
        }
    }
}

int main() {
    int test = 1;

    while (true) {
        int letter_count;

        cin >> letter_count;

        if (letter_count == 0) {
            break;
        }

        CodeLetter code_letter_table[letter_count];

        for (int i = 0; i < letter_count; i++) {
            std::string code;
            char letter;

            cin >> letter >> code;

            code_letter_table[i] = CodeLetter{code, letter};
        }

        std::sort(code_letter_table, code_letter_table + letter_count, [](const CodeLetter &a, const CodeLetter &b) {
            return a.letter < b.letter;
        });

        std::string message;

        cin >> message;

        bool stop = false;
        int incomplete_nodes = 1;

        std::vector<std::string> decoded_messages;
        decode(letter_count, code_letter_table, message, "", decoded_messages);

        cout << "Case #" << test << endl;

        for (int i = 0; i < decoded_messages.size(); i++) {
            cout << decoded_messages[i] << endl;
        }

        cout << endl;

        test++;
    }

    return 0;
}