class Solution(object):
    def solve(self, inputStr):
        inputList = [int(i) for i in inputStr.split()]
        target = sum(inputList)
        halfTarget = target // 2
        halfLen = len(inputList) // 2
        prevList = inputList[:halfLen]
        postList = inputList[halfLen:]
        prevSums = {i:set() for i in range(halfLen+1)}
        postSums = {i:set() for i in range(halfLen+1)}
        for i in range(2 ** halfLen):
            prevSum = 0
            postSum = 0
            numCnt = 0
            for j in range(halfLen):
                if (i>>j)&1:
                    prevSum += prevList[j]
                    postSum += postList[j]
                    numCnt += 1
            prevSums[numCnt].add(prevSum)
            postSums[numCnt].add(postSum)
        minDiff = float('inf')
        for i in range(halfLen+1):
            prevSet = sorted(list(prevSums[i]))
            postSet = sorted(list(postSums[halfLen-i]))
            prevIndex, postIndex = 0, len(postSet) - 1
            while postIndex >= 0 and prevIndex < len(prevSet):
                sumHalf = prevSet[prevIndex] + postSet[postIndex]
                if sumHalf == halfTarget:
                    return target - halfTarget * 2
                elif sumHalf > halfTarget:
                    postIndex -= 1
                    minDiff = min(minDiff, 2 * sumHalf - target)
                else:
                    prevIndex += 1
                    minDiff = min(minDiff, target - 2 * sumHalf)
        return minDiff