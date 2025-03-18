"""
Anagrams.
"""


def sort_strip(string):
    """
    Remove os espaços e ordena.
    """

    return sorted(string.replace(' ', ''))


def format_pair(anagram_pair):
    """
    Formata os pares.
    """

    first, second = sorted(anagram_pair)

    return first + ' = ' + second


test_count = int(input())

input()  # Skip blank line

for test in range(test_count):
    lines = []
    anagrams_pairs = []

    if test > 0:
        print()

    while True:
        try:
            line = input()

            if line == '':
                break
        except EOFError:
            break

        lines.append(line)

    for i, line_a in enumerate(lines):
        for j in range(i + 1, len(lines)):
            if sort_strip(line_a) == sort_strip(lines[j]):
                anagrams_pairs.append(format_pair((line_a, lines[j])))

    for anagram_pair in sorted(anagrams_pairs):
        print(anagram_pair)
