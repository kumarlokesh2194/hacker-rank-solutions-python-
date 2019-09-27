def count_substring(string, sub_string):

    real_count = 0
    for i in range(len(string)):
        count = 0
        if(string[i]==sub_string[0]):
            for j in range(len(sub_string)):
                if((i+j)<(len(string))):
                    if(string[i+j]==sub_string[j]):
                        count+=1
                if(count == len(sub_string)):
                    real_count+=1
                    count = 0

    return real_count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
