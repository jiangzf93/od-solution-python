class Solution(object):

    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        costs = [int(c) for c in inputLines[0].split()]
        days = [int(d) for d in inputLines[1].split()]
        dp = [0] * 366
        for i in range(1, 366):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(i-1, 0)] + costs[0],
                            dp[max(i-3, 0)] + costs[1],
                            dp[max(i-7, 0)] + costs[2],
                            dp[max(i-30, 0)] + costs[3])
        return dp[365]