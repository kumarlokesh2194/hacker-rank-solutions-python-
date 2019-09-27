# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools
[s, k] = input().split()
k = int(k)
res = []
for i in itertools.combinations_with_replacement(s, k):
    res += [''.join(sorted(i))]
for i in sorted(res):
    print (i)
