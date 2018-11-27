"""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers. """
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minlist=[]
    maxlist=[]
    minimum=min(arr)
    maximum=max(arr)
    minlist=arr
    maxlist=arr
    minlist.remove(maximum)
    sumlist1=sum(minlist)
    maxlist.append(maximum)
    maxlist.remove(minimum)
    sumlist2=sum(maxlist)
    print(sumlist1,sumlist2)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
