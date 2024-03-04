class Solution(object):
    def solve(self, inputStr):
        houses = [int(h) for h in inputStr.split()]
        if len(houses) > 8:
            return -1
        elif len(houses) == 8:
            return max(houses)
        else:
            left, right = 0, max(houses)
            result = float('inf')
            while left <= right:
                mid = (left + right) // 2
                hours = 0
                for h in houses:
                    hours += h // mid
                    if h % mid > 0:
                        hours += 1
                if hours <= 8:
                    result = min(result, mid)
                    right = mid - 1
                else:
                    left = mid + 1
            return result