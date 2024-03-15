class Solution(object):

    def solve(self, inputStr):
        strLen = len(inputStr)
        dbStr = inputStr * 2
        inputLen = len(dbStr)
        dp = [[] for _ in range(8)]
        dp[0].append(-1)
        pattern = 0
        result = 0
        for i in range(inputLen):
            s = dbStr[i]
            if s == 'l':
                pattern ^= (1<<0)
            elif s == 'o':
                pattern ^= (1<<1)
            elif s == 'x':
                pattern ^= (1<<2)
            currDp = dp[pattern]
            currDp.append(i)
            while currDp[-1] - currDp[0] > strLen:
                currDp.pop(0)
            dbLen = currDp[-1] - currDp[0]
            result = max(result, dbLen)
        return result