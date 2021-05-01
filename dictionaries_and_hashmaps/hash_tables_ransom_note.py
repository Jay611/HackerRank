import math
import os
import random
import re
import sys

from collections import defaultdict, Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dic = defaultdict(int)
    for word in magazine:
        dic[word] += 1
        
    for word in note:
        if dic[word] == 0: return False
        dic[word] -= 1
        
    return True


    """ Using Counter """
    # print(Counter(magazine)) # Counter({'two': 1, 'times': 1, 'three': 1, 'is': 1, 'not': 1, 'four': 1})
    # print(Counter(note))  # Counter({'two': 2, 'times': 1, 'is': 1, 'four': 1})
    # print(Counter(note) - Counter(magazine))  # Counter({'two': 1})
    # return (Counter(note) - Counter(magazine)) == {}
        
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))