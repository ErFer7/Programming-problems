# -*- coding: utf-8 -*-

while True:

    caseStr = input().split()
    caseMap = map(int, caseStr)
    case = list(caseMap)

    if case[0] == 0 and case [1] == 0:
        break

    ticketsStr = input().split()
    ticketsMap = map(int, ticketsStr)
    tickets = list(ticketsMap)

    lst = []
    dLst = []
    duplicateCount = 0

    for ticket in tickets:

        if ticket not in lst:

            lst.append(ticket)
        else:

            if ticket not in dLst:

                duplicateCount += 1
                dLst.append(ticket)
    
    print(duplicateCount)