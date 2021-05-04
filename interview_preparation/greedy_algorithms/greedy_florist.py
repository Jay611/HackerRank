def getMinimumCost(k, c):
    c = sorted(c, reverse=True)
    def getSubCost(k, c, i = 1):
        if len(c) <= k:
            return sum(c) * i
        else:
            return sum(c[:k]) * i + getSubCost(k, c[k:], i + 1)
            
    return getSubCost(k, c)

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    

    print(minimumCost)
