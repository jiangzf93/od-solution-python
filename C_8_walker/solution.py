class Solution(object):
    def __init__(self):
        self.count = 0
        self.dr = [0, 0, 1, -1]
        self.dc = [1, -1, 0, 0]

    def dfs(self, row, col, visited, path_length, direction):
        if path_length > self.count:
            self.count = path_length
        visited[row][col] = 1
        for i in range(4):
            newR = row + self.dr[i]
            newC = col + self.dc[i]
            if newR >= 0 and newR < self.rows and newC >= 0 and newC < self.cols and not visited[newR][newC]:
                hDiff = self.matrix[newR][newC] - self.matrix[row][col]
                newD = hDiff / abs(hDiff)
                if newD != direction:
                    self.dfs(newR, newC, visited, path_length + 1, newD)
        visited[row][col] = 0

    def solve(self, inptStr):
        inputLines = inptStr.split('\n')
        inputDim = inputLines[0].split()
        self.rows = int(inputDim[0])
        self.cols = int(inputDim[1])
        inputRows = [i.split() for i in inputLines[1:self.rows+1]]
        self.matrix = [[int(n) for n in r[:self.cols]] for r in inputRows]

        for r in range(self.rows):
            for c in range(self.cols):
                visited = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
                self.dfs(r, c, visited, 0, 0)

        return self.count