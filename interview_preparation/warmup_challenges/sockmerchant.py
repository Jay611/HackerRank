import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
  # Write your code here
  dic = {}
  for a in ar:
    dic.update({a: dic.get(a) + 1 if dic.get(a) is not None else 1})
    
  return sum(d//2 for d in dic.values())

n = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)

print(result)

