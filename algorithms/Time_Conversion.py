"""Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock. """
import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(str1):
    #
    # Write your code here.
    #

    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]

if __name__ == '__main__':


    s = input()

    result = timeConversion(s)

    print(result + '\n')


