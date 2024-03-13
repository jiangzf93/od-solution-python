import heapq

class Solution(object):

    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        inputOrder = [int(o) for o in inputLines[0].split(',')]
        targetOrder = [int(t) for t in inputLines[1].split(',')]
        orderIndex, targetIndex = 0, 0
        currQueue = []
        outOrder = []
        while orderIndex < len(inputOrder):
            currQueue.append(inputOrder[orderIndex])
            while True:
                if len(currQueue) > 1 and currQueue[-1] == targetOrder[targetIndex]:
                    currQueue.pop()
                    targetIndex += 1
                    outOrder.append('R')
                elif len(currQueue) > 0 and currQueue[0] == targetOrder[targetIndex]:
                    currQueue.pop(0)
                    targetIndex += 1
                    outOrder.append('L')
                else:
                    break
            orderIndex += 1
        return 'NO' if currQueue else ''.join(outOrder)