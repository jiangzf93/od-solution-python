class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        memberCount = int(inputLines[0])
        memberIncome = [int(i) for i in inputLines[1].split()[:memberCount]]
        familyIncome = memberIncome.copy()
        familyRelations = inputLines[2:]
        for r in familyRelations:
            relation = r.split()
            parent = int(relation[0]) - 1
            child = int(relation[1]) - 1
            familyIncome[parent] += memberIncome[child]
        return max(familyIncome)