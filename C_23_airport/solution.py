class Solution(object):
    def solve(self, inputStr):
        airlines = inputStr.split(',')
        sortedLine = sorted(airlines, key=lambda x: (x[:2], x[2:]))
        return ','.join(sortedLine)