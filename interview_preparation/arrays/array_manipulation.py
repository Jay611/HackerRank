import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    res = [0] * (n + 1)
    s = m = 0
        
    for a, b, k in queries:
        res[a - 1] += k
        res[b] -= k
    
    for r in res:
        s = s + r
        if s > m:
            m = s

    return m
    
if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    
    print(result)
