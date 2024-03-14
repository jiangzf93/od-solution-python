class UF(object):
    def __init__(self, n):
        self.count = n
        self.root = [i for i in range(n)]

    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]
    
    def union(self, left, right):
        rootL = self.find(left)
        rootR = self.find(right)
        if rootL != rootR:
            self.root[left] = rootR
            self.count -= 1

class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        totalNums= int(inputLines[0])
        affected = [int(a) for a in inputLines[1].split(',')]
        uf = UF(totalNums)
        for a in range(1, len(affected)):
            uf.union(a-1, a)
        for row in range(totalNums):
            rowRecord = inputLines[row+2].split(',')
            for col in range(totalNums):
                if col != row and rowRecord[col] == '1':
                    uf.union(row, col)
        return totalNums - uf.count + 1 - len(affected)