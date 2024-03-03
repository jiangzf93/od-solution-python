class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        dims = inputLines[0].split()
        rows = int(dims[0])
        cols = int(dims[1])
        matrix = [r.split()[:cols] for r in inputLines[1:rows+1]]
        landMap = {}
        for r in range(rows):
            for c in range(cols):
                mark = matrix[r][c]
                if mark == '0':
                    continue
                if mark not in landMap:
                    landMap[mark] = {
                        'minR': r,
                        'minC': c,
                        'maxR': r,
                        'maxC': c
                    }
                else:
                    currMap = landMap[mark]
                    if r > currMap['maxR']:
                        currMap['maxR'] = r
                    if c > currMap['maxC']:
                        currMap['maxC'] = c
        maxArea = 0
        for land in landMap:
            map = landMap[land]
            area = (map['maxR'] - map['minR'] + 1) * (map['maxC'] - map['minC'] + 1)
            maxArea = max(maxArea, area)
        return maxArea