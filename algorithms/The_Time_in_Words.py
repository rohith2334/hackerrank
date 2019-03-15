import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    names=["zero", "one","two","three","four","five", "six", "seven", "eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine"]
   if(m<30 and m>=00):
        if(m==0):
            string= "{} o' clock".format(names[h])
        else:
            if(m==1):
                string="{} minute past {}".format(names[m],names[h])
            elif(m==15):
                string="quarter past {}".format(names[h]) 
            else:
                string="{} minutes past {}".format(names[m],names[h])      
    else:
        m=60-m
        if(m==30):
            string="half past {}".format(names[h])
        elif(m==15):
            string="quarter to {}".format(names[h+1])    
        else:    
            string="{} minutes to {}".format(names[m],names[h+1])
    return string   

if __name__ == '__main__':
  
    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    print(result )

   
