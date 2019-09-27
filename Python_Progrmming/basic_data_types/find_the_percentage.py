if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum_ = 0
    for key_ in student_marks:
        if(key_ == query_name):
            marks = student_marks.get(key_)
            for j in marks:
                sum_+=j
    print("%.2f"%(sum_/3))
