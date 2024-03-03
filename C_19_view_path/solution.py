class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        inputDims = inputLines[0].split()
        rows = int(inputDims[0])
        cols = int(inputDims[1])
        matrix = [[int(c) for c in r.split()[:cols]] for r in inputLines[1:rows+1]]
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    dp[r+1][c+1] = 1
                elif matrix[r][c] == 1:
                    dp[r+1][c+1] = 0
                else:
                    dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1]
        return dp[rows][cols]