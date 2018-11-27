if __name__ == '__main__':
    n = int(input())
    l1=[]
    l2=[]
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        men=("{0:.2f}".format(sum(scores)/(len(scores))))
        student_marks[name] = men
    query_name = input()
    print(student_marks[query_name])

