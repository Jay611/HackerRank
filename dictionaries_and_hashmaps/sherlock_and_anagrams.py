import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    substrings = [''.join(sorted(s[i:j+1])) for i in range(len(s)) for j in range(i, len(s))]
    return sum([(v*(v-1))//2 for _, v in Counter(substrings).most_common()])

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        
        print(result)