

class Solution(object):

    def solve(self, inputStr):
        str1, str2 = inputStr.split()[:2]
        len1, len2 = len(str1), len(str2)
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for r in range(len1+1):
            for c in range(len2+1):
                if r == 0:
                    dp[r][c] = c
                elif c == 0:
                    dp[r][c] = r
                else:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + 1
                    if str1[r-1] == str2[c-1]:
                        dp[r][c] = min(dp[r-1][c-1] + 1, dp[r][c])
        return dp[len1][len2]