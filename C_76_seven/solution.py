from collections import defaultdict
class Solution(object):
    def solve(self, inputNum):
        dp = [0] * (inputNum+1)
        dp[8] = 1
        dp[9] = 1
        for i in range(10, inputNum+1):
            dp[i] = dp[i-2] + 2*dp[i-3] + dp[i-4]
        return dp[inputNum]