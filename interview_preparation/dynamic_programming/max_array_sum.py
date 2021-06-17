# Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset. It is possible that the maximum sum is 0, the case when all elements are negative.


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    a, b = 0, 0

    for val in arr:
        a, b = b, max(a, a + val, b, val)

    return b


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)
    
    print(res)
