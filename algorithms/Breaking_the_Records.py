#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    first=scores[0]
    tempbest=scores[0]
    tempworst=scores[0]
    count=0
    dec=0
    for i in range(0,len(scores)):
        if(scores[i]>tempbest):
            count+=1
            tempbest=scores[i]
        elif(scores[i]<tempworst):
            dec+=1
            tempworst=scores[i]
    return count,dec

if __name__ == '__main__':


    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))



