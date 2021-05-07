import math

def minimumPasses(m, w, p, n):
    # Write your code here
    
    # Wrong answer!!
    
    # num_prod = x = 0
    # count = 0
    # while num_prod < n:
    #     print('num_prod', num_prod)
    #     num_resource = num_prod // p
    #     num_prod -= (num_resource * p)
    #     print('num_prod', num_prod, 'num_resource', num_resource)
    #     x = (num_resource - m + w) / 2
    #     x1 = max(0, math.ceil(x))
    #     x2 = max(0, math.floor(x))
        
    #     x_max = x1 if (m + x1) * (w + num_resource - x1) >= (m + x2) * (w + num_resource - x2) else x2
        
    #     m += x_max
    #     w += (num_resource - x_max)

    #     num_prod += m * w
    #     count += 1
    #     print('count', count, 'num_prod', num_prod)
    # return count

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)
    
    print(result)