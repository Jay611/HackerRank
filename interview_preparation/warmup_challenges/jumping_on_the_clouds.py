import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    if len(c) == 1:
        return 0
    elif len(c) == 2:
        return 1
    elif len(c) > 2:
        if c[2] == 0:
            return 1 + jumpingOnClouds(c[2:])
        else:
            return 2 + jumpingOnClouds(c[3:])
        

if __name__ == '__main__':
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)