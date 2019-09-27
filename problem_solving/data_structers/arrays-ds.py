
import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    b = []
    for i in range(len(a)-1,-1,-1):
        b.append(a[i])
    return(' '.join(str(k) for k in b))
if __name__ == '__main__':

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(res)
