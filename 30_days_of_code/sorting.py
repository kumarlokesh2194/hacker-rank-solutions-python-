# day 20 buble sort
#!/bin/python3

import sys
t = 0
count = 0
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
for _ in range(len(a)):
    for i in range(len(a)):
        if(i+1)<(len(a)):
            if(a[i]>a[i+1]):
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t
                count+=1
                t = 0
print('Array is sorted in {} swaps.'.format(count))
print('First Element:',a[0])
print('Last Element:',a[-1])
# Write Your Code Here
