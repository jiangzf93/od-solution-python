import heapq

class Solution(object):
    def getPersonCount(self, limit):
        pCount = 0
        index = 0
        while index < len(self.dayList):
            dayLeft = limit
            while index < len(self.dayList) and self.dayList[index] <= dayLeft:
                dayLeft -= self.dayList[index]
                index += 1
            pCount += 1
        return pCount


    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        self.dayList = sorted([int(d) for d in inputLines[0].split()])
        self.employees = int(inputLines[1])
        left, right = max(self.dayList), sum(self.dayList)
        while left <= right:
            mid = (left + right) // 2
            hCount = self.getPersonCount(mid)
            if hCount == self.employees:
                right = mid - 1
            elif hCount > self.employees:
                left = mid + 1
            elif hCount < self.employees:
                right = mid - 1
        return left