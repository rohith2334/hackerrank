#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    Reverse = 0
    count=0
    for Number in range(i,j+1):
        reverse=int(str(Number)[::-1])
        abso=abs(Number-reverse)
        print(Number,reverse,abso)
        if(abso%k==0):
            count+=1
    return count


if __name__ == '__main__':


    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(str(result) + '\n')

