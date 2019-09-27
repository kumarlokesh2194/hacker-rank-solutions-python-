import itertools

k, m = map(int, input().strip().split(' '))
a = []
for i in range(k):
    a.append(input().split(' ')[1:])

mx = 0
for tp in itertools.product(*a):
    res = sum([int(x)**2 for x in tp]) % m
    if res > mx:
        mx = res

print(mx)
