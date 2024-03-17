import heapq
from collections import defaultdict

class Solution(object):

    def solve(self, inputStr):
        dependencies = inputStr.split()
        inDegree = defaultdict(int)
        graph = defaultdict(list)
        nodes = set()
        for dep in dependencies:
            end, start = dep.split('->')
            graph[start].append(end)
            inDegree[end] += 1
            nodes.add(start)
            nodes.add(end)
        nodes = list(nodes)
        q = []
        for node in nodes:
            if inDegree[node] == 0:
                heapq.heappush(q, node)
        result = []
        while q:
            currNode = heapq.heappop(q)
            result.append(currNode)
            for node in graph[currNode]:
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    heapq.heappush(q, node)
        return ' '.join(result)