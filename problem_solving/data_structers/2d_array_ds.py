
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    a = 0
    b = 0
    c = 0
    sum = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (i+2)<len(arr) and (j+2)<len(arr[0]):
                a = arr[i][j]+ arr[i][j+1]+arr[i][j+2]
                b = arr[i+1][j+1]
                c = arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                sum.append(a+b+c)
    return(max(sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
