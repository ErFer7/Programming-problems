# -*- coding: utf-8 -*- 

'''
Experiências
'''

test_count = int(input())

subjects = {'C': 0, 'R': 0, 'S': 0}
total_subjects = 0

for _ in range(test_count):

    count, subject_type = input().split()
    count = int(count)

    subjects[subject_type] += count
    total_subjects += count

print(f"Total: {total_subjects} cobaias")
print(f"Total de coelhos: {subjects['C']}")
print(f"Total de ratos: {subjects['R']}")
print(f"Total de sapos: {subjects['S']}")
print(f"Percentual de coelhos: {(subjects['C'] / total_subjects) * 100.0:.2f} %")
print(f"Percentual de ratos: {(subjects['R'] / total_subjects) * 100.0:.2f} %")
print(f"Percentual de sapos: {(subjects['S'] / total_subjects) * 100.0:.2f} %")
