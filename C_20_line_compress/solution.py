class Solution(object):
    def solve(self, inputStr):
        coords = [int(c) for c in inputStr.split()]
        cIndex = 0
        lineStart = [coords[0], coords[1]]
        result = []
        direction = (0, 0)
        while cIndex < len(coords):
            xCoord = coords[cIndex]
            yCoord = coords[cIndex+1]
            currDir = (xCoord - lineStart[0], yCoord - lineStart[1])
            if currDir != direction:
                result += [lineStart[0], lineStart[1]]
                direction = currDir
            lineStart = [xCoord, yCoord]
            cIndex += 2
        result += [lineStart[0], lineStart[1]]
        return ' '.join([str(r) for r in result])