# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import*
n = int(input())
dict = OrderedDict()
for i in range(n):
    names = input()
    if names in dict:
        dict[names] += 1
    else:
        dict[names] = 1
print(len(dict))
