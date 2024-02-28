class Solution(object):
    def solve(self, inptStr):
        inputLines = inptStr.split('\n')
        inputCount = int(inputLines[0])
        luckyNum = int(inputLines[1])
        luckyTrans = luckyNum + (1 if luckyNum >= 0 else -1)
        inputNums = [int(n) for n in inputLines[2].split()[:inputCount]]
        result = 0
        current = 0
        for num in inputNums:
            if num == luckyNum:
                current += luckyTrans
            else:
                current += num
            result = max(current, result)
        return result