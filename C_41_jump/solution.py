class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        numLen = int(inputLines[0])
        nums = [int(n) for n in inputLines[1].split()[:numLen]]
        pathLen = int(inputLines[2])
        maxScores = [0] * numLen
        for n in range(numLen):
            num = nums[n]
            maxScore = num
            for i in range(max(0, n-pathLen), n):
                maxScore = max(maxScore, num + maxScores[i])
            maxScores[n] = maxScore
        return maxScores[numLen-1]