#!/bin/python3
from fractions import gcd
import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    count=0
    for i in range(max(a),min(b)+1):
        between =  True
        for x in a:
            if i%x!=0:
                between = False
        for x in b:
            if x%i!=0:
                between = False
        if between==True:
            count+=1
    return(count)

if __name__ == '__main__':


    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    print(str(total) + '\n')


