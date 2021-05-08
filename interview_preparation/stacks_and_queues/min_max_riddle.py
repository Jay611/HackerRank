# Complete the riddle function below.
def riddle(arr):
    # complete this function
    s = []
    n = len(arr)
    left = [-1] * (n + 1)
    right = [n] * (n + 1)
    
    for i in range(n):
        while s and arr[s[-1]] >= arr[i]:
            s.pop()
        if s:
            left[i] = s[-1]
        s.append(i)
        
    s.clear()
    
    for i in range(n - 1, -1, -1):
        while s and arr[s[-1]] >= arr[i]:
            s.pop()
        if s:
            right[i] = s[-1]
        s.append(i)
        
    ans = [0] * (n + 1)
    
    for i in range(n):
        Len = right[i] - left[i] - 1
        ans[Len] = max(ans[Len], arr[i])
    
    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])

    return ans[1:]
        
    
if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)
    
    print(res)