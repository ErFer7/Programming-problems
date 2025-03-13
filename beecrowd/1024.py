# -*- coding: utf-8 -*-

'''
Criptografia
'''

test_count = int(input())

for _ in range(test_count):

    text = input()

    first_pass_text = ''

    # Primeira passada
    for character in text:

        if character.isalpha():
            first_pass_text += chr(ord(character) + 3)
        else:
            first_pass_text += character

    second_pass_text = first_pass_text[::-1]

    third_pass_text = second_pass_text[:len(second_pass_text) // 2]

    for i in range(len(second_pass_text) // 2, len(second_pass_text)):
        third_pass_text += chr(ord(second_pass_text[i]) - 1)

    print(third_pass_text)
