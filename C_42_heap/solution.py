class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        applyMemory = int(inputLines[0])
        usedMemory = [[int(i) for i in m.split()] for m in inputLines[1:]]
        unusedMemory = [[100, 0, 100]]
        for memory in usedMemory:
            memoryStart, memoryEnd = memory[0], memory[0] + memory[1]
            occupiedMemory = [x[0] for x in filter(lambda x: x[1][1] <= memoryStart and x[1][2] >= memoryEnd, enumerate(unusedMemory))][0]
            splitMemory = unusedMemory.pop(occupiedMemory)
            if memoryEnd < splitMemory[2]:
                unusedMemory.insert(occupiedMemory, [splitMemory[2] - memoryEnd, memoryEnd, splitMemory[2]])
            if memoryStart > splitMemory[1]:
                unusedMemory.insert(occupiedMemory, [memoryStart - splitMemory[1], splitMemory[1], memoryStart])
        unusedMemory.sort(key=lambda x: (x[0], x[1]))
        mIndex = 0
        while mIndex < len(unusedMemory):
            if unusedMemory[mIndex][0] >= applyMemory:
                break
            mIndex += 1
        if mIndex >= len(unusedMemory):
            return -1
        return unusedMemory[mIndex][1]