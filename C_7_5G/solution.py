class Solution(object):

    def mergeRoots(self, fromRoot, toRoot):
        for r in range(len(self.roots)):
            if self.roots[r] == fromRoot:
                self.roots[r] = toRoot

    def solve(self, inptStr):
        inputLines = inptStr.split('\n')
        numSites = int(inputLines[0])
        numPairs = int(inputLines[1])
        pairs = [[int(i) for i in p.split()] for p in inputLines[2:numPairs+2]]
        self.roots = [i for i in range(numSites+1)]
        for pair in pairs:
            site1 = pair[0]
            site2 = pair[1]
            connected = pair[3]
            if pair[3]:
                if self.roots[site1] != self.roots[site2] and connected:
                    self.mergeRoots(self.roots[site1], self.roots[site2])

        pairs = sorted(pairs, key = lambda x: x[2])
        cost = 0
        connected = False
        for pair in pairs:
            if len(list(set(self.roots[1:]))) == 1:
                connected = True
                break
            if pair[3] == 1:
                continue
            else:
                self.mergeRoots(self.roots[pair[0]], self.roots[pair[1]])
                cost += pair[2]
        if len(list(set(self.roots[1:]))) == 1:
            connected = True

        return cost if connected else -1