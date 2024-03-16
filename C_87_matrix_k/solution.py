
class Solution(object):
    def __init__(self):
        self.result = float('inf')

    def backtrace(self, row):
        if row == self.rows:
            sortedTrace = sorted(self.trace, reverse=True)
            self.result = min(self.result, sortedTrace[self.k-1])
            return
        for col in range(self.cols):
            if self.visited[col] == True:
                continue
            self.visited[col] = True
            self.trace.append(self.matrix[row][col])
            self.backtrace(row+1)
            self.trace.pop()
            self.visited[col] = False

    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        self.rows, self.cols, self.k = [int(n) for n in inputLines[0].split()]
        self.matrix = [[int(c) for c in row.split()] for row in inputLines[1:self.rows+1]]
        self.visited = [False] * self.cols
        self.trace = []
        self.backtrace(0)
        return self.result