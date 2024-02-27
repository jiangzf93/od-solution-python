class Solution(object):
    def solve(self, inputStr):
        result = 0
        lenInput = len(inputStr)
        if inputStr[0] == '0' and inputStr[1] == '0':
            result += 1
        if inputStr[lenInput-1] == '0' and inputStr[lenInput-2] == '0':
            result += 1
        for i in range(1, lenInput-1):
            if inputStr[i-1] == '0' and inputStr[i] == '0' and inputStr[i+1] == '0':
                result += 1
        return result