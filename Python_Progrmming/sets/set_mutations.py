# set mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
alist = list(map(int,input().split()))
aset = set(alist)
N = int(input())
for _ in range(N):
    nlist = input().split()
    command = nlist[0]
    value = nlist[1]
    if command == 'update':
        nvalues = list(map(int,input().split()))
        nset = set(nvalues)
        aset.update(nset)
    elif command == 'intersection_update':
        nvalues = list(map(int,input().split()))
        nset = set(nvalues)
        aset.intersection_update(nset)
    elif command == 'difference_update':
        nvalues = list(map(int,input().split()))
        nset = set(nvalues)
        aset.difference_update(nset)
    elif command == 'symmetric_difference_update':
        nvalues = list(map(int,input().split()))
        nset = set(nvalues)
        aset.symmetric_difference_update(nset)
print(sum(aset))
