class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        inputInfo = inputLines[0].split()
        featureCount = int(inputInfo[0])
        caseCount = int(inputInfo[1])
        preferences = [int(p) for p in inputLines[1:featureCount+1]]
        cases = [[int(p) for p in c.split()] for c in inputLines[featureCount+1:featureCount+caseCount+1]]
        orders = []
        for c in range(len(cases)):
            preference = 0
            for feature in cases[c]:
                preference += preferences[feature-1]
            orders.append([c+1, preference])
        orders.sort(key=lambda x: x[1], reverse=True)
        return '\n'.join([str(o[0]) for o in orders])