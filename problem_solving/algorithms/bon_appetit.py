
import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum1 = 0
    sum_ = 0
    for i in bill:
        sum_ +=i
    if(b==sum_/2):
        bill.remove(bill[k])
        for j in bill:
            sum1+=j
        print("%.0f"%(b-sum1/2))
    else:
        print("Bon Appetit")

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
