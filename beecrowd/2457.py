# -*- coding: utf-8 -*-

c = input()
txt = input().split()

total = len(txt)
cInst = 0.0

for w in txt:

    if c in w:

        cInst += 1.0

print("{:.1f}".format((cInst / float(total)) * 100.0))