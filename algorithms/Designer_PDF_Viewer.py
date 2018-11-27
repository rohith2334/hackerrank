#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    return (len(word) * max(h[ord(l) - ord('a')] for l in word))


if __name__ == '__main__':


    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result) + '\n')


