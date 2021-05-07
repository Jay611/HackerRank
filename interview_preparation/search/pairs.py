def pairs(k, arr):
    return len(set(arr) & set([item + k for item in set(arr)]))
    
    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)
    
    print(result)