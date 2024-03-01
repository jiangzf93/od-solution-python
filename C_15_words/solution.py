class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        wordCount = int(inputLines[0])
        words = inputLines[1:wordCount+1]
        chars = inputLines[wordCount+1]
        charStat = {}
        for c in chars:
            if c in charStat:
                charStat[c] += 1
            else:
                charStat[c] = 1
        result = 0
        for word in words:
            stat = charStat.copy()
            unmatched = 0
            for w in word:
                if w in stat and stat[w] > 0:
                    stat[w] -= 1
                else:
                    unmatched += 1
            if unmatched:
                if '?' in stat and stat['?'] >= unmatched:
                    result += 1
            else:
                result += 1
        return result