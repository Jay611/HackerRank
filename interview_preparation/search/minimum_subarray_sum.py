from bisect import bisect, insort

def maximumSum(a, m):
    # Write your code here
    
    cumulative_sums = []
    sum_so_far = 0
    max_sum = 0
    
    for i in range(len(a)):
        sum_so_far = (sum_so_far + a[i]) % m       
        pos = bisect(cumulative_sums, sum_so_far)
        d = 0 if pos == i else cumulative_sums[pos]
        max_sum = max(max_sum, (sum_so_far + m - d) % m)
        insort(cumulative_sums, sum_so_far)
    
    print(max_sum)
    
if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)
        
        print(result)