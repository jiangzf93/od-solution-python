class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        inputCount = inputLines[0].split()
        aCount = int(inputCount[0])
        bCount = int(inputCount[1])
        aList = [int(a) for a in inputLines[1].split()[:aCount]]
        bList = [int(b) for b in inputLines[2].split()[:bCount]]
        aSum = sum(aList)
        bSum = sum(bList)
        aSet = sorted(list(set(aList)))
        bSet = sorted(list(set(bList)))
        target = aSum - bSum
        aResult = 0
        bResult = 0
        hasResult = False
        for a in aSet:
            for b in bSet:
                if (a - b) * 2 == target:
                    aResult = a
                    bResult = b
                    hasResult = True
                    break
            if hasResult:
                break
        result = str(aResult) + ' ' + str(bResult)
        return result