# -*- coding: utf-8 -*-

finished = False
backTracking = False

mat = []
rot = []
lst = []
stack = []

n = int(input())

l, c = map(int, input().split())

l -= 1
c -= 1

for _ in range(n):

    mat.append(list(map(int, input().split())))
    rot.append([[-1, 0]] * n)

while not finished:

    if not backTracking:

        lst.append([l, c])
        stack.append([l, c])

    for i in range(4):

        if rot[l][c] == [-1, 0]:

            rot[l][c] = [0, 1]
        elif rot[l][c] == [0, 1]:

            rot[l][c] = [1, 0]
        elif rot[l][c] == [1, 0]:

            rot[l][c] = [0, -1]
        else:

            rot[l][c] = [-1, 0]
        
        if l + rot[l][c][0] >= 0 and l + rot[l][c][0] < n and c + rot[l][c][1] >= 0 and c + rot[l][c][1] < n and [l + rot[l][c][0], c + rot[l][c][1]] not in lst and mat[l + rot[l][c][0]][c + rot[l][c][1]] >= mat[l][c]:

            backTracking = False

            l += rot[l][c][0]
            c += rot[l][c][1]

            break
        elif i == 3:

            backTracking = True

            stack.remove(stack[-1])

            if len(stack) > 0:

                l = stack[-1][0]
                c = stack[-1][1]
            else:

                finished = True

print(len(lst))