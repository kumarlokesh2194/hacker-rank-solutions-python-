
import math
import os
import random
import re
import sys


def dynamicArray(N,Q):
    seq = []
    lastAnswer = 0
    l = []
    for i in range(N):
        seq.append([])

    for _ in range(len(Q)):
        a = Q[_][0]
        x = Q[_][1]
        y = Q[_][2]
        if a==1:
            value = (x^lastAnswer)%N
            seq[value].append(y)
        elif a==2:
            value = (x^lastAnswer)%N
            v = y%len(seq[value])
            lastAnswer = seq[value][v]
            l.append(lastAnswer)
    return(l)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
