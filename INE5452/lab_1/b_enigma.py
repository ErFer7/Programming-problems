"""
Enigma of the Jewelry Case.
"""

size = int(input())
matrix = []

for i in range(size):
    matrix.append(list(map(int, input().split())))

corners = (matrix[0][0], matrix[0][size - 1], matrix[size - 1][size -1], matrix[size - 1][0])

print(corners.index(min(corners)))
