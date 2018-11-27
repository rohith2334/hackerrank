"""rturn the score of the a or b win if a greater return a and b greater return b if both equal return 0"""
import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    wina = 0
    winb = 0
    list1 = []
    for i in range(0, 3):

        if (a[i] > b[i]):
            wina += 1
        elif (a[i] < b[i]):
            winb += 1
        else:
            wina += 0
            winb += 0
    list1.append(wina)
    list1.append(winb)
    return list1


if __name__ == '__main__':


    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))



