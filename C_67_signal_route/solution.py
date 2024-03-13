import heapq

class Solution(object):

    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        rows = int(inputLines[0])
        cols = int(inputLines[1])
        matrix = [[int(c) for c in row.split()[:cols]] for row in inputLines[2:rows+2]]
        cache = [[-1 for _ in range(cols)] for _ in range(rows)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        q = []
        startNum = matrix[0][0]
        heapq.heappush(q, [-startNum, [startNum, 0, 0]])
        while q:
            power, row, col = heapq.heappop(q)[1]
            if power < cache[row][col]:
                continue
            for d in directions:
                newRow = row + d[0]
                newCol = col + d[1]
                if newRow < 0 or newCol < 0 or newRow >= rows or newCol >= cols:
                    continue
                newPower = min(power, matrix[newRow][newCol])
                if newPower > cache[newRow][newCol]:
                    cache[newRow][newCol] = newPower
                    heapq.heappush(q, [-newPower, [newPower, newRow, newCol]])
        return cache[rows-1][cols-1]