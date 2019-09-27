# Enter your code here. Read input from STDIN. Print output to STDOUT

from __future__ import division
import collections

N = int(input())
columns = ','.join(input().split())
Student = collections.namedtuple('Student', columns)

sum = 0
for i in range(N):
    line = input().split()
    student = Student(*line)
    # print(student)
    sum += int(student.MARKS)

print(sum / N)
