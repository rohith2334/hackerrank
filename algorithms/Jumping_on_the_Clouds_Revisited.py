#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n=len(c)
    jump=0
    energy=100
    for i in range(0,len(c),k):
        jump=c[i]
        if(jump==0):
            energy-=1
        if(jump==1):
            energy-=3
    return energy


if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(str(result) + '\n')


