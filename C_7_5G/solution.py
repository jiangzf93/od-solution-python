class Solution(object):
    def getRoot(self, node):
        if (self.roots[node] == node):
            return node
        

    def solve(self, inptStr):
        inputLines = inptStr.split('\n')
        numSites = int(inputLines[0])
        numPairs = int(inputLines[1])
        pairs = [[int(i) for i in p.split()] for p in inputLines[2:numPairs+2]]
        self.roots = [i for i in range(numSites+1)]
        connParts = 0
        for pair in pairs:
            site1 = pair[0]
            site2 = pair[1]
            connected = pair[3]
            if roots[site1] != roots[site2] and connected:
                roots[site1] = roots[site2]
                connParts += 1
        for pair in pairs:
            if pair[3] == 1:
                continue


        return 1