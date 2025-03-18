# -*- coding: utf-8 -*-

'''
Loop Musical
'''

while True:

    peak_count = 0
    sample_count = int(input())

    if sample_count == 0:
        break

    magnitudes = list(map(int, input().split()))[:sample_count]

    for i in range(sample_count):

        if i == 0:

            if magnitudes[sample_count - 1] > magnitudes[i] and magnitudes[i] < magnitudes[i + 1]:

                peak_count += 1
            elif magnitudes[sample_count - 1] < magnitudes[i] and magnitudes[i] > magnitudes[i + 1]:

                peak_count += 1
        elif i == sample_count - 1:

            if magnitudes[i - 1] > magnitudes[i] and magnitudes[i] < magnitudes[0]:

                peak_count += 1
            elif magnitudes[i - 1] < magnitudes[i] and magnitudes[i] > magnitudes[0]:

                peak_count += 1
        else:

            if magnitudes[i - 1] > magnitudes[i] and magnitudes[i] < magnitudes[i + 1]:

                peak_count += 1
            elif magnitudes[i - 1] < magnitudes[i] and magnitudes[i] > magnitudes[i + 1]:

                peak_count += 1

    print(peak_count)
