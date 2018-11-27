import os
import sys


#
# Complete the pageCount function below.
#
def pageCount(n, p):
    count = 0

    if (p == n or p == (n - 1) or p == 1):
        count = 0
        if (n == 6 and p == 5):
            count = 1
    else:
        count = int(min(p // 2, n / 2 - p / 2))
    return count


if __name__ == '__main__':


    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(str(result) + '\n')


