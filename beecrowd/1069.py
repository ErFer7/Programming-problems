# -*- coding: utf-8 -*-

'''
Diamantes e Areia
'''

test_count = int(input())

for _ in range(test_count):

    test = input()

    stack = []
    total_diamonds = 0

    for char in test:

        if char == '<':
            stack.append(char)
        elif char == '>':

            if len(stack) > 0 and stack[-1] == '<':

                stack.pop()
                total_diamonds += 1

    print(total_diamonds)
