
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    s = sorted(arr)
    min_sum = 0
    max_sum = 0
    for i in range(0,4,1):
        min_sum+=s[i]
    for j in range(1,5,1):
        max_sum+=s[j]
    print(min_sum,max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
