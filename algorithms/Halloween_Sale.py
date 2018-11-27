import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    count=0
    if(s<p):
        return count
    while(s>=p):
        count+=1
        s=s-p
        if(p>m):
            p=p-d
        if(p<m):
            p=m
    return count

if __name__ == '__main__':


    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    print(str(answer) + '\n')


