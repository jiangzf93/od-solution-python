class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        employeeNum = int(inputLines[0])
        employeeList = [[int(e.split()[0]), int(e.split()[1])] for e in inputLines[1:employeeNum+1]]
        numList = sorted(list(set(map(lambda x: x[1], employeeList))))
        numSet = set()
        hasDup = False
        for e in employeeList:
            if e[1] not in numSet:
                numSet.add(e[1])
            else:
                hasDup = True
                break
        employeePairs = []
        numDict = {n: [] for n in numList}
        for e in employeeList:
            numDict[e[1]].append(e[0])
        if hasDup:
            for eList in numDict.values():
                for i in range(len(eList)):
                    for j in range(i+1, len(eList)):
                        e1 = eList[i]
                        e2 = eList[j]
                        if e1 > e2:
                            e1, e2 = e2, e1
                        employeePairs.append([e1, e2])
        else:
            numPairs = [[numList[0], numList[1]]]
            minDiff = numList[1] - numList[0]
            for n in range(1, len(numList)-1):
                n0 = numList[n]
                n1 = numList[n+1]
                diff = n1 - n0
                nArray = [n0, n1]
                if diff < minDiff:
                    numPairs = [nArray]
                    minDiff = diff
                elif diff == minDiff:
                    numPairs.append(nArray)
            for p in numPairs:
                for d1 in numDict[p[0]]:
                    for d2 in numDict[p[1]]:
                        if d1 > d2:
                            d2, d1 = d1, d2
                        employeePairs.append([d1, d2])

        sortedEmplyees = sorted(employeePairs, key=lambda x:(x[0], x[1]))
        return '\n'.join([str(e[0]) + ' ' + str(e[1]) for e in sortedEmplyees])