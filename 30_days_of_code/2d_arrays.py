#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    A = []

    for _ in range(6):
        A.append(list(map(int, input().rstrip().split())))

    smax = []

    for row in range(len(A) - 2):
        for column in range(len(A[row]) - 2):
            tl = A[row][column]
            tc = A[row][column + 1]
            tr = A[row][column + 2]
            mc = A[row + 1][column + 1]
            bl = A[row + 2][column]
            bc = A[row + 2][column + 1]
            br = A[row + 2][column + 2]
            s = tl + tc + tr + mc + bl + bc + br
            smax.append(s)

    print(max(smax))
