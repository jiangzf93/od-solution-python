class Solution(object):
    def findMinLarge(self, ele, lis):
        if len(lis) == 0:
            return 0
        left, right = 0, len(lis)-1
        while left <= right:
            mid = (left + right) // 2
            midVal = lis[mid]
            if midVal == ele:
                return mid
            elif midVal > ele:
                right = mid - 1
            else:
                left = mid + 1
        return right + 1

    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        taskNum = int(inputLines[0])
        timeLimit = int(inputLines[1])
        tasks = [l.split() for l in inputLines[2:taskNum+2]]
        tasks = [[int(t[0]), int(t[1])] for t in tasks]
        tasks = sorted(filter(lambda t: t[0] <= timeLimit, tasks), key=lambda t:t[0])
        result = []
        for task in tasks:
            reward = task[1]
            position = self.findMinLarge(reward, result)
            result.insert(position, reward)
            if len(result) > timeLimit or position >= task[0]:
                result.pop(0)
        return sum(result)