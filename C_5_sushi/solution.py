class Solution(object):
    def solve(self, inputStr):
        sushis = inputStr.split()
        cycleSushis = [int(sushi) for sushi in sushis] * 2
        addedSushis = [0] * len(cycleSushis)
        sushiStack = []
        for s in range(len(cycleSushis)):
            currSushi = cycleSushis[s]
            while(sushiStack and cycleSushis[sushiStack[-1]] > currSushi):
                sushiIndex = sushiStack.pop()
                addedSushis[sushiIndex] = cycleSushis[sushiIndex] + cycleSushis[s]
            sushiStack.append(s)
        while sushiStack:
            sushiIndex = sushiStack.pop()
            addedSushis[sushiIndex] = cycleSushis[sushiIndex]
        return ' '.join([str(s) for s in addedSushis[:len(sushis)]])