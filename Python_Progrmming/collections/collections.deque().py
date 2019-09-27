from collections import*
n = int(input())
d = deque()
for i in range(n):
    method = input().split()
    if method[0]=='append':
        d.append(int(method[1]))
    elif method[0]=='appendleft':
        d.appendleft(int(method[1]))
    elif method[0]=='pop':
        d.pop()
    elif method[0]=='popleft':
        d.popleft()
print(' '.join(str(k) for k in d))
