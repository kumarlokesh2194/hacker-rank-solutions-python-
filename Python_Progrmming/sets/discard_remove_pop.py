n = input()
s = set(map(int, input().split()))
t=int(input())
for i in range(t):
    p=input().split()
    if p[0]=="remove":
        s.remove(int(p[1]))
    elif p[0]=="discard":
        s.discard(int(p[1]))
    else:
        s.pop()
print(sum(list(s)))
