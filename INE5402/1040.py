# -*- coding: utf-8 -*-

wLst = [2.0, 3.0, 4.0, 1.0]

a, b, c, d = map(float, input().split())

average = round((a * wLst[0] + b * wLst[1] + c * wLst[2] + d * wLst[3]) / sum(wLst), 1)

print("Media: %.1f" % average)

if average >= 7.0:

    print("Aluno aprovado.")
elif average >= 5.0:

    print("Aluno em exame.")

    gR = float(input())

    print("Nota do exame: %.1f" % gR)

    recAverage = round((gR + average) / 2.0, 1)

    if recAverage >= 5.0:

        print("Aluno aprovado.")
    else:

        print("Aluno reprovado.")

    print("Media final: %.1f" % recAverage)
else:

    print("Aluno reprovado.")