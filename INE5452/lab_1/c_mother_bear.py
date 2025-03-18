"""
Mother bear.
"""

translation = str.maketrans({'.': '', ',': '', '!': '', '?': '', ' ': ''})

while True:
    value = input()

    if value == 'DONE':
        break

    clean_str = value.translate(translation).lower()

    if clean_str == ''.join(list(reversed(clean_str))):
        print('You won\'t be eaten!')
    else:
        print('Uh oh..')
