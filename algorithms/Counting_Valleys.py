import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=0
    flag=False
    valley=0
    for i in s:
        if i=='D':
            level-=1
        elif i=='U':
            level+=1
        if flag==True and level>=0:
            valley+=1
            flag=False
        if level<0:
            flag=True
    return valley

if __name__ == '__main__':


    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(str(result) + '\n')


