class Solution(object):
    def solve(self, inputList):
        sortedList = sorted(inputList, key=lambda x:x[0])
        idx = 0
        result = []
        while idx < len(sortedList):
            currentItem = sortedList[idx]
            idx += 1
            while idx < len(sortedList) and sortedList[idx][0] <= currentItem[1]:
                currentItem = [currentItem[0], sortedList[idx][1]]
                idx += 1
            result.append(currentItem)
        return result