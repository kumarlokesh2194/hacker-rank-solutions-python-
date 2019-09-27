from collections import*
K = int(input())
klist = list(map(int,input().split()))
d = OrderedDict()
for _ in klist:
    if _ in d:
        d[_]+=1
    else:
        d[_]=1
for i in d.keys():
    if d[i] == 1:
        print(i)
        break
