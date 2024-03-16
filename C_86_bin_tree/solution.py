class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def buildMidOrder(self, node):
        if not node:
            return
        self.buildMidOrder(node.left)
        self.midOrder.append(str(node.val))
        self.buildMidOrder(node.right)
        return

    def dealTree(self, node):
        if not node:
            return 0
        leftVal = self.dealTree(node.left)
        rightVal = self.dealTree(node.right)
        currVal = node.val
        node.val = leftVal + rightVal
        return node.val + currVal

    def buildTree(self, midOrder, preOrder):
        if not preOrder:
            return None
        elif len(preOrder) == 1:
            return BinaryTree(preOrder[0])
        else:
            rootVal = preOrder[0]
            root = BinaryTree(rootVal)
            rootIndex = midOrder.index(rootVal)
            root.left = self.buildTree(midOrder[0:rootIndex], preOrder[1:rootIndex+1])
            root.right = self.buildTree(midOrder[rootIndex+1:], preOrder[rootIndex+1:])
            return root

    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        midOrder = [int(n) for n in inputLines[0].split()]
        preOrder = [int(n) for n in inputLines[1].split()]
        tree = self.buildTree(midOrder, preOrder)
        self.dealTree(tree)
        self.midOrder = []
        self.buildMidOrder(tree)
        return ' '.join(self.midOrder)