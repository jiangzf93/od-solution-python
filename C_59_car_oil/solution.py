import heapq

class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        dims = inputLines[0].split(',')
        rows = int(dims[0])
        cols = int(dims[1])
        matrix = [[int(c) for c in row.split(',')[:cols]] for row in inputLines[1:rows+1]]
        costTable = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        costTable[0][0] = matrix[0][0]
        dirctions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        q = []
        heapq.heappush(q, [matrix[0][0], [matrix[0][0], 0, 0, False, matrix[0][0]]])
        result = float('inf')
        while q:
            point = heapq.heappop(q)
            cost, row, col, added, firstCost = point[1]
            if cost > costTable[row][col]:
                continue
            for d in dirctions:
                newRow = row + d[0]
                newCol = col + d[1]
                if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
                    continue
                if matrix[newRow][newCol] == 0:
                    continue
                if matrix[newRow][newCol] == -1:
                    minCost = firstCost if added else cost
                    heapq.heappush(q, [0, [0, newRow, newCol, True, minCost]])
                    continue
                newVal = matrix[newRow][newCol] + cost
                if newVal > 100:
                    continue
                if newVal < costTable[newRow][newCol]:
                    costTable[newRow][newCol] = newVal
                    minCost = firstCost if added else newVal
                    if newRow == rows - 1 and newCol == cols - 1:
                        result = min(result, minCost)
                    else:
                        heapq.heappush(q, [newVal, [newVal, newRow, newCol, added, minCost]])

        return -1 if costTable[rows-1][cols-1] == float('inf') else result