class Solution(object):
    def solve(self, inputStr):
        oneChar = inputStr[0]
        charCount = 0
        result = 0
        for char in inputStr:
            if char == oneChar:
                charCount += 1
            else:
                charCount -= 1
            if charCount == 0:
                result += 1
        return result