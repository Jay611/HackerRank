import math
import os
import random
import re
import sys

from collections import Counter
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    ca = Counter(a)
    cb = Counter(b)
    ca.subtract(cb)
    return sum(abs(i) for i in ca.values())
    
if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)
    
    print(res)