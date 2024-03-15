import heapq

class TreeNode(object):
    def __init__(self, weight, height = 1, left = None, right = None):
        self.weight = weight
        self.height = height
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.weight == other.weight:
            return self.height <= other.height
        return self.weight < other.weight

class Solution(object):
    def __init__(self):
        self.midOrder = []

    def traverse(self, node):
        if node == None:
            return
        self.traverse(node.left)
        self.midOrder.append(str(node.weight))
        self.traverse(node.right)

    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        nodeNum = int(inputLines[0])
        nodes = inputLines[1].split()
        nodeQueue = []
        for n in range(nodeNum):
            heapq.heappush(nodeQueue, TreeNode(int(nodes[n]))) 
        while len(nodeQueue) > 1:
            leftNode = heapq.heappop(nodeQueue)
            rightNode = heapq.heappop(nodeQueue)
            newWeight = leftNode.weight + rightNode.weight
            newHeight = max(leftNode.height, rightNode.height) + 1
            parentNode = TreeNode(newWeight, newHeight, leftNode, rightNode)
            heapq.heappush(nodeQueue, parentNode)
        self.traverse(heapq.heappop(nodeQueue))
        return ' '.join(self.midOrder)