def minimumAbsoluteDifference(arr):
    # Write your code here
    arr = sorted(arr)
    return min([abs(arr[i] - arr[i+1]) for i in range(len(arr) - 1)])

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    
    print(result)