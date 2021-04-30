import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    dic = {}
    is_too_chaotic = False
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(q) - 1):
            if q[i] > q[i + 1]:
                if dic.get(q[i]) == 2: 
                    is_too_chaotic = True
                    break
                dic.update({q[i]: dic.get(q[i]) + 1 if dic.get(q[i]) is not None else 1})
                q[i], q[i + 1] = q[i + 1], q[i]
                swapped = True
                
    if is_too_chaotic:
        print('Too chaotic')
    else:
        print(sum(dic.values()))

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
