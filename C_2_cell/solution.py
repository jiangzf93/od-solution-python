class Solution(object):
    
    def parseCell(self, cellIndex, visited):
        cell = self.cells[cellIndex]
        leftIndex = cell.find('<')
        rightIndex = cell.find('>')
        if leftIndex < 0 and rightIndex < 0:
            return cell
        if leftIndex < 0 or rightIndex < 0:
            return -1
        if cell.find('<', leftIndex + 1) >= 0:
            return -1
        if cell.find('>', rightIndex + 1) >= 0:
            return -1
        if rightIndex - leftIndex != 2:
            return -1
        refIndex = ord(cell[leftIndex+1]) - ord('A')
        if refIndex == cellIndex or refIndex >= len(self.cells) or visited[refIndex] != 0:
            return -1
        visited[refIndex] = 1
        parseResult = self.parseCell(refIndex, visited)
        if parseResult == -1:
            return -1
        else:
            self.cells[cellIndex] = cell[:leftIndex] + parseResult + cell[rightIndex+1:]
            return self.cells[cellIndex]


    def solve(self, str):
        self.cells = str.split(',')
        for cellIndex in range(len(self.cells)):
            visited = [0] * len(self.cells)
            parseResult = self.parseCell(cellIndex, visited)
            if parseResult == -1:
                return '-1'
        return ','.join(self.cells)