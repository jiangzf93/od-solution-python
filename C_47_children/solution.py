
class Solution(object):
    def solve(self, inputStr):
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        inputLines = inputStr.split('\n')
        dim = int(inputLines[0])
        matrix = [[0 for _ in range(dim)] for _ in range(dim)]
        visited = [[False for _ in range(dim)] for _ in range(dim)]
        startRow, startCol, endRow, endCol = 0, 0, 0, 0
        for r in range(dim):
            rowNums = inputLines[1+r].split(' ')
            for c in range(dim):
                num = int(rowNums[c])
                matrix[r][c] = num
                if num == -3:
                    startRow = r
                    startCol = c
                elif num == -2:
                    endRow = r
                    endCol = c
                elif num == -1:
                    visited[r][c] = True
        start = [startRow, startCol]
        q = [start]
        depth = 0
        foundPath = False
        while q:
            depth += 1
            qLen = len(q)
            for _ in range(qLen):
                currRow, currCol = q.pop(0)
                for d in directions:
                    newRow = currRow + d[0]
                    newCol = currCol + d[1]
                    if newRow < 0 or newRow >= dim or newCol < 0 or newCol >= dim or visited[newRow][newCol]:
                        continue
                    if newRow == endRow and newCol == endCol:
                        foundPath = True
                        break
                    if not visited[newRow][newCol]:
                        visited[newRow][newCol] = True
                        q.append([newRow, newCol])
                if foundPath:
                    break
            
            if foundPath:
                break
        if not foundPath:
            return -1
        q = [start]
        candies = [[0 for _ in range(dim)] for _ in range(dim)]
        candies[start[0]][start[1]] = 0
        maxCandies = 0
        for _ in range(depth):
            qLen = len(q)
            for _ in range(qLen):
                currRow, currCol = q.pop(0)
                currentCandies = candies[currRow][currCol]
                for d in directions:
                    newRow = currRow + d[0]
                    newCol = currCol + d[1]
                    if newRow < 0 or newRow >= dim or newCol < 0 or newCol >= dim or matrix[newRow][newCol] == -1:
                        continue
                    if newRow == endRow and newCol == endCol:
                        maxCandies = max(maxCandies, currentCandies)
                    else:
                        newCandies = matrix[newRow][newCol] + currentCandies
                        if newCandies > candies[newRow][newCol]:
                            candies[newRow][newCol] = newCandies
                            q.append([newRow, newCol])
        return maxCandies