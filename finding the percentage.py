if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    i = 0
    total = 0
    for mark in student_marks[query_name]:
        i += 1
        total += mark
    avg = total / i
    print("{:.2f}".format(avg))