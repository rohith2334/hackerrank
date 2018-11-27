#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    val=0
    floordiv=0
    res=0
    my_dict = {i:ar.count(i) for i in ar}
    for i in my_dict:
        val=my_dict[i]
        floordiv=val//2
        res+=floordiv
    return res




if __name__ == '__main__':


    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')


