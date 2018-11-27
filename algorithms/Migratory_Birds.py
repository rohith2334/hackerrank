

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    a=[]
    for i in range(1,6):
        a.append(arr.count(i))
    return(a.index(max(a))+1)

if __name__ == '__main__':


    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')


