"""Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line."""
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    n=len(arr)
    for i in range(0,len(arr)):
        if(arr[i]>0):
            pos+=1
        elif(arr[i]<0):
            neg+=1
        else:
            zer+=1
    posratio=round(pos/n,6)
    negratio=round(neg/n,6)
    zeroratio=round(zer/n,6)
    print(posratio)
    print(negratio)
    print(zeroratio)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
