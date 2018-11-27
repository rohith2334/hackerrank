"""Given an array of integers, find the sum of its elements."""
import os
import sys


#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    num1 = 0
    for i in range(0, len(ar)):
        num1 += ar[i]
    return num1


if __name__ == '__main__':


    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(str(result) + '\n')


