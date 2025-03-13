# -*- coding: utf-8 -*-

seconds = int(input())

minutes = seconds / 60
hours = minutes / 60

print("%d:%d:%d" % (int(hours), int(minutes % 60), int(seconds % 60)))