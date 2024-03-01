class Solution(object):
    def solve(self, inputStr):
        octNum, luckyNum, divider = [int(n) for n in inputStr.split()]
        result = 0
        while(octNum > 0):
            if octNum % divider == luckyNum:
                result += 1
            octNum //= divider
        return result