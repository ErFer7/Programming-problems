"""
Lavaspar.
"""

from bisect import insort


def process_match(possible_match: list[str],
                  word: tuple[str],
                  possible_match_cells: list[tuple[int, int]],
                  cell_matches: dict[tuple[int, int], set[tuple[str]]]) -> None:
    """
    Processa os matches
    """

    if tuple(possible_match) == word:
        for cell in possible_match_cells:
            cell_matches[cell].add(tuple(possible_match))


line_count, column_count = map(int, input().split())
matrix = []
cell_matches = {(i, j): set() for j in range(column_count) for i in range(line_count)}

words = []

for _ in range(line_count):
    matrix.append(input())

word_count = int(input())

for _ in range(word_count):
    word = tuple(sorted(input()))
    words.append(word)

letters = set()

for word in words:
    for letter in word:
        letters.add(letter)

for i in range(line_count):
    for j in range(column_count):
        letter = matrix[i][j]

        if letter in letters:
            for word in words:
                if letter in word:
                    word_length = len(word)

                    # Leste
                    if j + word_length - 1 < column_count:
                        possible_match = []
                        possible_match_cells = []

                        for k in range(word_length):
                            possible_match_cells.append((i, j + k))
                            insort(possible_match, matrix[i][j + k])

                        process_match(possible_match, word, possible_match_cells, cell_matches)

                    # Sul
                    if i + word_length - 1 < line_count:
                        possible_match = []
                        possible_match_cells = []

                        for k in range(word_length):
                            possible_match_cells.append((i + k, j))
                            insort(possible_match, matrix[i + k][j])

                        process_match(possible_match, word, possible_match_cells, cell_matches)

                    # Sudeste
                    if i + word_length - 1 < line_count and j + word_length - 1 < column_count:
                        possible_match = []
                        possible_match_cells = []

                        for k in range(word_length):
                            possible_match_cells.append((i + k, j + k))
                            insort(possible_match, matrix[i + k][j + k])

                        process_match(possible_match, word, possible_match_cells, cell_matches)

                    # Sudoeste
                    if i + word_length - 1 < line_count and j - word_length + 1 >= 0:
                        possible_match = []
                        possible_match_cells = []

                        for k in range(word_length):
                            possible_match_cells.append((i + k, j - k))
                            insort(possible_match, matrix[i + k][j - k])

                        process_match(possible_match, word, possible_match_cells, cell_matches)

special_cell_count = 0

for _, cell_match in cell_matches.items():
    if len(cell_match) > 1:
        special_cell_count += 1

print(special_cell_count)
