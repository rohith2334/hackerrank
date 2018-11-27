import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(squares, d, m):
    count = 0
    for i in range(len(squares) - m + 1):
        count += int(sum(squares[i:i + m]) == d)
    return count


if __name__ == '__main__':


    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')


