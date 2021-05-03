import math
import os
import random
import re
import sys

from collections import defaultdict
#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    count = 0
    freq = defaultdict(int)
    
    def findMedian(idx):
        total_count = 0
        for i in range(201): 
            if i in freq:
                total_count = total_count + freq[i]
            if total_count >= idx:
                return i
        
    for i in range(len(expenditure)-1):
        freq[expenditure[i]] += 1
        if i >= d - 1:
            if d % 2 == 0:
                median = (findMedian(d // 2) + findMedian(d // 2 + 1)) / 2
            else:
                median = findMedian(d / 2)
            
            if expenditure[i + 1] >= median * 2:
                count += 1
            
            freq[expenditure[i-d+1]]-=1
            
    return count
        
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    
    print(result)