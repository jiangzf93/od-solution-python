class Solution(object):
    def __init__(self):
        self.maxWin = 0
        self.maxCount = 0
        self.winCount = 0
        self.trace = 0

    def backtrace(self):
        if self.trace == self.n:
            if self.winCount > self.maxWin:
                self.maxWin = self.winCount
                self.maxCount = 1
            elif self.winCount == self.maxWin:
                self.maxCount += 1
            return
        for i in range(self.n):
            if self.visited[i]:
                continue
            num = self.arr1[i]
            comp = self.arr2[self.trace]
            self.visited[i] = True
            self.trace += 1
            if num > comp:
                self.winCount += 1
            self.backtrace()
            self.visited[i] = False
            self.trace -= 1
            if num > comp:
                self.winCount -= 1
            
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        self.arr1 = [int(a) for a in inputLines[0].split()]
        self.arr2 = [int(a) for a in inputLines[1].split()]
        self.n = len(self.arr1)
        self.visited = [False] * self.n
        self.backtrace()
        return self.maxCount