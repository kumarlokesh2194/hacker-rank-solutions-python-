def minion_game(S):

    n = len(S)
    stuart = 0
    kevin = 0

    for i in range(n):
        if S[i] in ('A', 'E', 'I', 'O', 'U'):
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print ('Kevin', kevin)
    elif stuart > kevin:
        print ('Stuart', stuart)
    else:
        print ('Draw')
        # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)
