#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    l=[int(i) for i in str(n)]
    spl=0
    for i in range(0,len(l)):
        if(l[i]!=0):
            if(n%l[i]==0):
                spl+=1
    return spl

if __name__ == '__main__':


    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(str(result) + '\n')


