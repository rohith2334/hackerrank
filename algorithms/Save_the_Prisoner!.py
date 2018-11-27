#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(p, m, id):
    if((m+id-1)%p==0):
        return(p);
    else:
        return((m+id-1)%p)

if __name__ == '__main__':


    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        p = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(p, m, s)

        print(str(result) + '\n')


