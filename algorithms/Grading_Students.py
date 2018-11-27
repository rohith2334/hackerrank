import os
import sys


#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    l1 = []
    for i in grades:
        if (i >= 38):
            num = int(i + (5 - i % 5))
            sub = num - i
            if (sub < 3):
                l1.append(num)
            else:
                l1.append(i)
        else:
            l1.append(i)

    return l1


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))

