# -*- coding: utf-8 -*-

while True:

    try:

        h, m = map(int, input().split(":"))

        hB = format(bin(h))[2:]
        mB = format(bin(m))[2:]

        hB = "0" * (4 - len(hB)) + hB
        mB = "0" * (6 - len(mB)) + mB

        hBOut = []
        mBOut = []

        for i in hB:

            if i == "1":

                hBOut.append("o")
            else:

                hBOut.append(" ")

        for i in mB:

            if i == "1":

                mBOut.append("o")
            else:

                mBOut.append(" ")

        print(" ____________________________________________\n"                                                                                 + \
              "|                                            |\n"                                                                                + \
              "|    ____________________________________    |_\n"                                                                               + \
              "|   |                                    |   |_)\n"                                                                                  + \
              "|   |   8         4         2         1  |   |\n"                                                                                + \
              "|   |                                    |   |\n"                                                                                + \
              "|   |   {0}         {1}         {2}         {3}  |   |\n".format(hBOut[0], hBOut[1], hBOut[2], hBOut[3])                         + \
              "|   |                                    |   |\n"                                                                                + \
              "|   |                                    |   |\n"                                                                                + \
              "|   |   {0}     {1}     {2}     {3}     {4}     {5}  |   |\n".format(mBOut[0], mBOut[1], mBOut[2], mBOut[3], mBOut[4], mBOut[5]) + \
              "|   |                                    |   |\n"                                                                                + \
              "|   |   32    16    8     4     2     1  |   |_\n"                                                                                  + \
              "|   |____________________________________|   |_)\n"                                                                                  + \
              "|                                            |\n"                                                                                + \
              "|____________________________________________|\n")

    except EOFError:
        break