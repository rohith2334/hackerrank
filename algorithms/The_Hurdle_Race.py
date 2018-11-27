#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    maxi=max(height)
    portion=0
    if(maxi>k):
        portion=maxi-k
    else:
        portion=0
    return portion


if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(str(result) + '\n')


