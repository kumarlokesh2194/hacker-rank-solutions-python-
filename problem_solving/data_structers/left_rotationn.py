def array_left_rotation(a, n, k):
    for i in range(k):
        f = a[0]
        a.remove(f)
        a.append(f)
    return a


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(' '.join(map(str,answer)))
