from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.windowDict = defaultdict(int)
        self.numsDict = defaultdict(int)
        self.colDicts = []
        self.result = float('inf')

    def checkMin(self, index):
        for num in self.numsDict:
            if (self.windowDict[num] - self.colDicts[index][num]) < self.numsDict[num]:
                return False
        for num in self.colDicts[index]:
            self.windowDict[num] -= self.colDicts[index][num]
        return True


    def checkValid(self):
        for num in self.numsDict:
            if self.windowDict[num] < self.numsDict[num]:
                return False
        return True


    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        rows, cols = [int(n) for n in inputLines[0].split()]
        matrix = [[int(n) for n in row.split()[:cols]] for row in inputLines[1:rows+1]]
        numLen = int(inputLines[rows+1])
        nums = [int(n) for n in inputLines[rows+2].split()[:numLen]]
        
        for n in nums:
            self.numsDict[n] += 1
        for c in range(cols):
            colDict = defaultdict(int)
            for r in range(rows):
                colDict[matrix[r][c]] += 1
            self.colDicts.append(colDict)
        left, right = 0, 0
        
        while right < cols:
            colDict = self.colDicts[right]
            for n in colDict:
                self.windowDict[n] += colDict[n]
            if self.checkValid():
                self.result = min(self.result, right - left + 1)
            while left < right and self.checkMin(left):
                left += 1
            right += 1
        return self.result