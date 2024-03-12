import heapq

class Solution(object):
    def solve(self, inputStr):
        lights, timePerRoad, rowStart, colStart, rowEnd, colEnd = eval(inputStr)
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        rows, cols = len(lights), len(lights[0])
        minTimes = [[[float('inf')] * 4 for _ in range(cols)] for _ in range(rows)]
        q = []
        for i in range(4):
            minTimes[rowStart][colStart][i] = 0
            heapq.heappush(q, [0, [rowStart, colStart, i, 0]])
        while q:
            currRow, currCol, currDir, currTime = heapq.heappop(q)[1]
            if currTime > minTimes[currRow][currCol][currDir]:
                continue
            for d in range(4):
                if d == 2:
                    continue
                newDir = (currDir + d) % 4
                newRow = currRow + directions[newDir][0]
                newCol = currCol + directions[newDir][1]
                if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
                    continue
                newTime = currTime + timePerRoad
                if d != 1:
                    newTime += lights[currRow][currCol]
                if newTime < minTimes[newRow][newCol][newDir]:
                    minTimes[newRow][newCol][newDir] = newTime
                    heapq.heappush(q, [newTime, [newRow, newCol, newDir, newTime]])
        return min(minTimes[rowEnd][colEnd][0], minTimes[rowEnd][colEnd][1], minTimes[rowEnd][colEnd][2])