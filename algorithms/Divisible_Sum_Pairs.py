import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
l1=[]
def divisibleSumPairs(n, k, ar):
    sum=0
    num=0
    for i in range(0,len(ar)):
        for j in range(i+1,len(ar)):
            sum=ar[i]+ar[j]
            if(sum%k==0):
                num+=1
    return num


if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(str(result) + '\n')


