"""Given a square matrix, calculate the absolute difference between the sums of its diagonals. """
import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    l = sum(arr[i][i] for i in range(n))
    r = sum(arr[i][n-i-1] for i in range(n))
    return abs(l - r)
   # absolutediff=abs(sum_first_diagonal-sum_second_diagonal)
    #return absolutediff

if __name__ == '__main__':


    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')

