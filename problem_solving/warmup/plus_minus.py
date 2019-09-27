

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in range(0,len(arr),1):
        if(arr[i]>0):
            positive+=1
        elif(arr[i]<0):
            negative+=1
        elif(arr[i]==0):
            zero+=1
    p_fraction = positive/len(arr)
    n_fraction = negative/len(arr)
    z_fraction = zero/len(arr)
    print('%.6f'%p_fraction)
    print('%.6f'%n_fraction)
    print('%.6f'%z_fraction)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
