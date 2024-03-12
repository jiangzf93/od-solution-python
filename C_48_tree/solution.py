class Solution(object):
    def __init__(self):
        self.maxLen = 0

    def backtrace(self, index):
        if index >= len(self.nums) or self.nums[index] == -1:
            return 0
        leftLen = self.backtrace(index*2+1)
        rightLen = self.backtrace(index*2+2)
        maxPath = max(leftLen, rightLen) + self.nums[index]
        self.maxLen = max(self.maxLen, maxPath)
        return maxPath


    def solve(self, inputStr):
        self.nums = [int(n) for n in inputStr.split()]
        self.backtrace(0)
        return self.maxLen