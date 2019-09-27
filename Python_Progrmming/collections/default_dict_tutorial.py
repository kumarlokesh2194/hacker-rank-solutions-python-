# default dictionary tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
m,n = list(map(int,input().split()))
a=[]
b=[]
for i in range(m):
    a.append(input())
for j in range(n):
    b.append(input())
for k in range(len(b)):
    p=[]
    for l in range(len(a)):
        if(b[k]==a[l]):
            p.append(l+1)
        if(b[k]!=any(a[l])):
            z = -1
    if(len(p)>0):
        print(' '.join(str(m) for m in p))
    else:
        print(z)
