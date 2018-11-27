

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(n_price, m_price, s):
    #
    # Write your code here.
    #
    flag=0
    mp=0
    for i in range(len(n_price)):
        for j in range(len(m_price)):
            if (n_price[i]+m_price[j])<=s and (n_price[i]+m_price[j])>mp:
                a,b=n_price[i],m_price[j]
                flag=1
                mp = n_price[i]+m_price[j]
    if flag==0:
        return(-1)
    else:
        return(a+b)

if __name__ == '__main__':


    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(str(moneySpent) + '\n')


