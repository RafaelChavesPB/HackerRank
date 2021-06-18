#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    importants = []
    luck = 0
    for it in contests:
        if it[1]:
            importants.append(it[0])
        else:
            luck+=it[0]
    importants.sort(reverse = True)
    for it in importants:
        if k>0:
            luck+=it
            k-=1
        else:
            luck-=it
    return luck
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
