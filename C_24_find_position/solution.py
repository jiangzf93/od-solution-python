class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        heights = [int(h) for h in inputLines[0].split(',')]
        target = int(inputLines[1])
        left, right = 0, len(heights) - 1
        while left <= right:
            mid = (left + right) // 2
            if heights[mid] == target:
                return mid
            elif heights[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right + 2