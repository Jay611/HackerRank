from bisect import bisect
# Complete the triplets function below.
def triplets(a, b, c):
    a, b, c = sorted(set(a)), set(b), sorted(set(c))
    return sum(bisect(a, n2) * bisect(c, n2) for n2 in b)
    
    
if __name__ == '__main__':

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)
    
    print(ans)