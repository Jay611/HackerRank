import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    height = count_valley = 0
    for p in path:
        height += 1 if p == 'U' else -1
        if height == 0 and p == 'U':
            count_valley += 1
    return count_valley
            
        

if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

