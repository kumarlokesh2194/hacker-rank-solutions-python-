# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
count = 1
dictionary_ = OrderedDict()
for i in range(n):
    item_ = input()
    if item_ in dictionary_:
        dictionary_[item_]+=1
    else:
        dictionary_[item_] = 1
print(len(dictionary_))
print(' '.join(map(str,dictionary_.values())))
