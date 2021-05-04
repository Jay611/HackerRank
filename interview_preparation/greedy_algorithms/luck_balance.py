def luckBalance(k, contests):
    # Write your code here
    luck = 0
    for lck, imp in sorted(contests, reverse=True):
        if k > 0 or not imp:
            luck += lck
            k -= imp
        else:
            luck -= lck
    return luck

    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    
    print(result)