# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
dictionary = OrderedDict()
for i in range(n):
    item = input().split()
    item_name = ' '.join(item[:-1])
    net_price = item[-1]
    net_price = int(net_price)
    if item_name in dictionary:
        dictionary[item_name]+=net_price
    else:
        dictionary[item_name] = net_price
for j in dictionary:
    print(j,dictionary[j])
