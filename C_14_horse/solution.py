class Solution(object):
    def __init__(self):
        self.dirctions = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

    def bfs(self, row, col, step):
        stepMatrix = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]
        currStep = 0
        points = [(row, col)]
        while currStep <= step:
            buffer = []
            for point in points:
                r, c= point
                if stepMatrix[r][c] == -1:
                    stepMatrix[r][c] = currStep
                for d in self.dirctions:
                    newR = r + d[0]
                    newC = c + d[1]
                    if newR >= 0 and newR < self.rows and newC >= 0 and newC < self.cols and stepMatrix[newR][newC] == -1:
                        buffer.append((newR, newC))
            points = buffer
            currStep += 1
        for r in range(self.rows):
            for c in range(self.cols):
                if stepMatrix[r][c] == -1 or self.resultMatrix[r][c] == -1:
                    self.resultMatrix[r][c] = -1
                else:
                    self.resultMatrix[r][c] += stepMatrix[r][c]



    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        inputDim = inputLines[0].split()
        self.rows = int(inputDim[0])
        self.cols = int(inputDim[1])
        matrix = [['.' if c == '.' else int(c) for c in r.split()[:self.cols]] for r in inputLines[1:self.rows+1]]
        self.resultMatrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                if matrix[r][c] == '.':
                    continue
                else:
                    self.bfs(r, c, matrix[r][c])

        result = float('inf')
        for r in range(self.rows):
            for c in range(self.cols):
                if self.resultMatrix[r][c] != -1:
                    result = min(result, self.resultMatrix[r][c])
                
        return result