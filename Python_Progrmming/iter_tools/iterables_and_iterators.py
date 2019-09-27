# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import*
n = int(input())
s = input().split()
k = int(input())
c = 0
d = list(permutations(s,k))
for _ in d:
    if 'a' in _:
        c+=1
prob = c/len(d)
print('%0.4f'%prob)
