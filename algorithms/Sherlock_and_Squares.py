#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    numOfSquares = 0;
    x = 1;
    while(x*x < a):
        x+=1
    while(x*x <= b):
        numOfSquares+=1;
        x+=1
    return numOfSquares;


if __name__ == '__main__':


    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        print(str(result) + '\n')


