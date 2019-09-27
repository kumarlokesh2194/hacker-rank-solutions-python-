def average(array):
    set_ = set(array)
    new_set = list(set_)
    new_list = list(map(int,new_set))
    length = len(new_list)
    s = 0
    for i in new_list:
        s+=i
    return(s/length)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
