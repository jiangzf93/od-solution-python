class Solution(object):
    def getProdInfo(self, i):
        return [self.risks[i], self.profits[i], self.limits[i]]

    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        prodNum, totalMoney, totalRisk = [int(n) for n in inputLines[0].split()]
        self.profits = [int(n) for n in inputLines[1].split()[:prodNum]]
        self.risks = [int(n) for n in inputLines[2].split()[:prodNum]]
        self.limits = [int(n) for n in inputLines[3].split()[:prodNum]]
        combines = [0] * prodNum
        maxProfit = 0
        for i in range(prodNum):
            risk, profit, limit = self.getProdInfo(i)
            if risk > totalRisk:
                continue
            monoMoney = min(limit, totalMoney)
            monoProfit = monoMoney * profit
            if monoProfit > maxProfit:
                combines = [0] * prodNum
                combines[i] = monoMoney
                maxProfit = monoProfit
            for j in range(i+1, prodNum):
                sRisk, sProfit, sLimit = self.getProdInfo(j)
                if sRisk + risk > totalRisk:
                    continue
                fMoney, sMoney = 0, 0
                if limit + sLimit > totalMoney:
                    if profit > sProfit:
                        fMoney = min(totalMoney, limit)
                        sMoney = totalMoney - fMoney
                    else:
                        sMoney = min(totalMoney, sLimit)
                        fMoney = totalMoney - sMoney
                else:
                    fMoney = limit
                    sMoney = sLimit
                doubleProfit = fMoney * profit + sMoney * sLimit
                if doubleProfit > maxProfit:
                    combines = [0] * prodNum
                    combines[i] = fMoney
                    combines[j] = sMoney
                    maxProfit = doubleProfit
        
        return ' '.join([str(c) for c in combines])