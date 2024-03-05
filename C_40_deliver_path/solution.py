class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        countInfo = inputLines[0].split()
        customerCount = int(countInfo[0])
        distanceCount = int(countInfo[1])
        customerMap = {}
        distanceMatrix = [[float('inf') for _ in range(customerCount+1)] for _ in range(customerCount+1)]
        customers = [[int(i) for i in c.split()] for c in inputLines[1:customerCount+1]]
        for c in range(customerCount):
            customerId, distance = customers[c]
            customerMap[customerId] = c + 1
            distanceMatrix[0][c+1] = distance
            distanceMatrix[c+1][0] = distance
        distances = [[int(i) for i in d.split()] for d in inputLines[customerCount+1:customerCount+distanceCount+1]]
        for d in range(distanceCount):
            index1 = customerMap[distances[d][0]]
            index2 = customerMap[distances[d][1]]
            distance = distances[d][2]
            distanceMatrix[index1][index2] = distance
            distanceMatrix[index2][index1] = distance
        queue = [[0,0]]
        cache = [[float('inf') for _ in range(customerCount+1)] for i in range(2 ** customerCount)]
        cache[0][0] = 0
        while queue:
            current = queue.pop(0)
            for i in range(customerCount+1):
                if i == current[0]:
                    continue
                newPos = current[1]
                if i != 0:
                    newPos |= (1 << (i-1))
                newDistance = cache[current[1]][current[0]] + distanceMatrix[current[0]][i]
                if newDistance < cache[newPos][i]:
                    cache[newPos][i] = newDistance
                    queue.append([i, newPos])
        return cache[2**customerCount-1][0]