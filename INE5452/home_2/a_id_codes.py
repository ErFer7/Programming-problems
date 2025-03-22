"""
ID Codes.
"""

while True:
    code = input().strip()

    if code == '#':
        break

    result = 'No Successor'
    swap_index = None
    swap_char = ''

    for i in range(len(code) - 1, 0, -1):
        if i - 1 >= 0 and code[i - 1] < code[i]:
            swap_index = i - 1
            swap_char = code[swap_index]
            break

    if swap_index is not None:
        code = list(code)
        prefix = code[:swap_index]
        suffix_swap_index = None

        for i in range(len(code) - 1, swap_index, -1):
            if code[i] > swap_char:
                suffix_swap_index = i
                break

        code[swap_index], code[suffix_swap_index] = code[suffix_swap_index], swap_char
        code[swap_index + 1:] = reversed(code[swap_index + 1:])

        result = ''.join(code)

    print(result)
