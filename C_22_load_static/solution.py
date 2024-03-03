class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        historyCount = int(inputLines[0])
        directories = inputLines[1:historyCount+1]
        keyInfo = inputLines[historyCount+1].split()
        level = int(keyInfo[0])
        keyword = keyInfo[1]
        result = 0
        for directory in directories:
            path = directory.split('/')
            if len(path) > level and path[level] == keyword:
                result += 1
        return result