class Solution(object):
    def solve(self, inputStr):
        wa, wb, wt, pa, pb = [int(i) for i in inputStr.split()]
        maxA = wt // wa
        maxProfit = 0
        for a in range(1, maxA + 1):
            b = (wt - a * wa) // wb
            if b > 0:
                maxProfit = max(a * pa + b * pb, maxProfit)
        return maxProfit