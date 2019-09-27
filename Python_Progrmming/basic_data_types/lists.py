if __name__ == '__main__':
    n = int(input())
    l_ = []
    for i in range(n):
        list_ = input().split()
        l_.append(list_)
    l = []
    for t in l_:
        l1 = (t[0],*(int(v) for v in t[1:]))
        l.append(l1)

    b=[]
    for s in l:
        if(s[0]=='insert'):
            b.insert(s[1],s[2])
        elif(s[0]=='append'):
            b.append(s[1])
        elif(s[0]=='remove'):
            b.remove(s[1])
        elif(s[0]=='sort'):
            b.sort()
        elif(s[0]=='pop'):
            b.pop()
        elif(s[0]=='reverse'):
            b.reverse()
        elif(s[0]=='print'):
            print(b)
