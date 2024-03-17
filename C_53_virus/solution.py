import heapq

class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        nodeNum = int(inputLines[0])
        linkNum = int(inputLines[1])
        links = [[int(n) for n in row.split()] for row in inputLines[2:2+linkNum]]
        startNode = int(inputLines[2+linkNum])
        graph = [[] for _ in range(nodeNum+1)]
        dists = [float('inf') for _ in range(nodeNum+1)]
        dists[startNode] = 0
        for link in links:
            graph[link[0]].append([link[1], link[2]])
        q = []
        heapq.heappush(q, [0, startNode])
        while q:
            currDist, currNode = heapq.heappop(q)
            if currDist > dists[currNode]:
                continue
            for node in graph[currNode]:
                newNode, newDist  = node[0], node[1]+currDist
                if newDist < dists[newNode]:
                    dists[newNode] = newDist
                    heapq.heappush(q, [newDist, newNode])
        
        return -1 if max(dists[1:]) == float('inf') else max(dists[1:])