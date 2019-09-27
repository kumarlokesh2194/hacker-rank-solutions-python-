#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    length = len(arr)-1
    print(' '.join(str(arr[i]) for i in range(length,-1,-1)))
