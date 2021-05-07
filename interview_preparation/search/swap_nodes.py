#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def getDepth(self, root, depth = 1):
        if root:
            dl = self.getDepth(root.left, depth+1)
            dr = self.getDepth(root.right, depth+1)
            depth = max(dl,dr)
        else:
            depth -= 1
        return depth
            
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
    
    def swap(self, root, depth, height = 1):
        if root:
            if depth == height:
                temp = root.left
                root.left = root.right
                root.right = temp
            else:
                self.swap(root.left, depth, height+1)
                self.swap(root.right, depth, height+1)
                

                
def swapNodes(indexes, queries):
    # Write your code here
    nodes = [Node(i) for i in range(1, len(indexes) + 1)]
    for i, index in enumerate(indexes):
        if index[0] > 0:
            nodes[i].left = nodes[index[0] - 1]
        if index[1] > 0:
            nodes[i].right = nodes[index[1] - 1]

    res = []
    for k in queries:
        H = [k * i for i in range(len(indexes)) if k * i <= nodes[0].getDepth(nodes[0])]
        for h in H:
            nodes[0].swap(nodes[0], h)
        res.append(nodes[0].inorderTraversal(nodes[0]))
    return res

if __name__ == '__main__':

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    print(result)
