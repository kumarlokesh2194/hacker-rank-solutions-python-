# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
sizes = Counter(list(map(int,input().split())))
n = int(input())
money = 0
for i in range(n):
    size,price = list(map(int,input().split()))
    if(sizes[size]>0):
        sizes[size]-=1
        money+=price
print(money)
