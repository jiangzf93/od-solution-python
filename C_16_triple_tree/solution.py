class TipleTree(object):
    def __init__(self, val):
        self.value = val
        self.leftNode = None
        self.midNode = None
        self.rightNode = None

    def addNode(self, node):
        if node.value < self.value - 500:
            if self.leftNode:
                return self.leftNode.addNode(node) + 1
            else:
                self.leftNode = node
                return 1
        elif node.value > self.value + 500:
            if self.rightNode:
                return self.rightNode.addNode(node) + 1
            else:
                self.rightNode = node
                return 1
        else:
            if self.midNode:
                return self.midNode.addNode(node) + 1
            else:
                self.midNode = node
                return 1

class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        nodeNum = int(inputLines[0])
        nodes = [int(n) for n in inputLines[1].split()[:nodeNum]]
        root = TipleTree(nodes[0])
        maxDepth = 1
        for n in range(1, len(nodes)):
            node = TipleTree(nodes[n])
            maxDepth = max(maxDepth, root.addNode(node) + 1)
        return maxDepth