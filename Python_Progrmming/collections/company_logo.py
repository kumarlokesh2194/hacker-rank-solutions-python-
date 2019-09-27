import math
import os
import random
import re
import sys
from collections import*
if __name__ == '__main__':
    s = sorted(input())
    dict = OrderedDict()
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    m = (sorted(dict.items(),key = lambda x:x[1],reverse = True))
    for j in range(3):
        print(' '.join(str(k) for k in m[j]))
