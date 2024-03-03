class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        projectCount = int(inputLines[0])
        weights = [int(w) for w in inputLines[1].split()]
        hots = []
        for p in range(projectCount):
            project = inputLines[2+p].split()
            hots.append([project[0], project[1]*weights[0], project[2]*weights[1], project[3]*weights[2], project[4]*weights[3], project[5]*weights[4]])
        hots = sorted(hots, key=lambda x: x[1], reverse=True)
        return '\n'.join(list(map(lambda x: x[0], hots)))