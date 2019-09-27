

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    n = []
    for i in grades:
        if(i>=40):
            rem = i%5
            if(rem>=3):
                n.append(i+(5-rem))
            else:
                n.append(i)
        elif(37<i<40):
            rem=i%5
            n.append(i+(5-rem))
        else:
            n.append(i)
    return n


    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
