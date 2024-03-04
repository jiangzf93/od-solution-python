class Solution(object):
    def solve(self, inputStr):
        x, y, cntx, cnty = [int(i) for i in inputStr.split()[:4]]
        left, right = 0, 10 ** 9
        while left < right:
            mid = (left + right) // 2
            if mid // (x*y) + cntx + cnty > mid:
                left = mid + 1
            else:
                right = mid
        return left