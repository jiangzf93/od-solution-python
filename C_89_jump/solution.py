
class Solution(object):
    def solve(self, inputStr):
        nums = [int(n) for n in inputStr.split()]
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for n in range(1, len(nums)):
            dp[n+1] = max(dp[n], dp[n-1]+nums[n])
        return dp[len(nums)]