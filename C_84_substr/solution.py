class Solution(object):

    def solve(self, inputStr):
        subStr, mainStr = inputStr.split('\n')
        subLen, mainLen = len(subStr), len(mainStr)
        subPos, mainPos = 0, 0
        while subPos < subLen and mainPos < mainLen:
            if subStr[subPos] == mainStr[mainPos]:
                subPos += 1
            mainPos += 1
        return (mainPos - 1) if subPos == subLen else -1