class Solution(object):
    def __init__(self):
        self.maxLen = 0
        self.trace = []
        self.result = None
        self.directions = [[-1,0],[0,1],[1,0],[0,-1]]

    def backtrace(self, index, s):
        currRow = index[0]
        currCol = index[1]
        if currRow < 0 or currRow >= self.dim or currCol < 0 or currCol >= self.dim:
            return
        if self.matrix[currRow][currCol] != self.seq[s] or self.visited[currRow][currCol]:
            return
        self.trace.append([currRow, currCol])
        if s == self.seqLen - 1:
            if not self.result:
                self.result = self.trace.copy()
            return
        self.visited[currRow][currCol] = True
        for d in self.directions:
            newRow = currRow + d[0]
            newCol = currCol + d[1]
            self.backtrace([newRow, newCol], s+1)
        self.trace.pop()
        self.visited[currRow][currCol] = False
        return 


    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        self.seqLen = int(inputLines[0])
        self.seq = [int(n) for n in inputLines[1].split()[:self.seqLen]]
        self.dim = int(inputLines[2])
        self.matrix = [[int(n) for n in row.split()[:self.dim]] for row in inputLines[3:self.dim+3]]
        for r in range(self.dim):
            for c in range(self.dim):
                self.visited = [[False for _ in range(self.dim)] for _ in range(self.dim)]
                self.backtrace([r, c], 0)
                if self.result:
                    break
            if self.result:
                break
        if not self.result:
            return 'error'
        return ' '.join([str(r[0]) + ' ' + str(r[1]) for r in self.result])