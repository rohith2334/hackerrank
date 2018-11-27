import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    res=[]
    for i in range(0,q):
        catAmouse=abs(z-x)
        catBmouse=abs(z-y)
        if(catAmouse<catBmouse):
            return("Cat A")
        elif(catBmouse<catAmouse):
            return("Cat B")
        else:
            return("Mouse C")


if __name__ == '__main__':


    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result + '\n')


