class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        gemCount = int(inputLines[0])
        if not gemCount:
            return 0
        gems = [int(g) for g in inputLines[1:gemCount+1]]
        maxAmount = int(inputLines[gemCount+1])
        left, right = 0, 0
        currAmount = gems[0]
        maxCount = 0
        while True:
            if currAmount <= maxAmount:
                maxCount = max(maxCount, right - left + 1)
                right += 1
                if right >= len(gems):
                    break
                currAmount += gems[right]
            else:
                if left < right:
                    currAmount -= gems[left]
                    left += 1
                else:
                    right += 1
                    if right >= len(gems):
                        break
                    currAmount += gems[right]
        return maxCount