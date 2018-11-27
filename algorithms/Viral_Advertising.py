#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    a=5//2
    like = 0
    while n>0:
        like += a
        a = (a*3)//2
        n-=1
    return(like)

if __name__ == '__main__':


    n = int(input())

    result = viralAdvertising(n)

    print(str(result) + '\n')


