class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        recordCount = int(inputLines[0])
        records = [int(r) for r in inputLines[1].split()[:recordCount]]
        threshold = int(inputLines[2])
        pageStatic = {}
        for record in records:
            if record in pageStatic:
                pageStatic[record] += 1
            else:
                pageStatic[record] = 1
        outputList = sorted(filter(lambda x:x[1]>=threshold, pageStatic.items()), key=lambda x:(-x[1], x[0]))
        result = str(len(outputList)) 
        if len(outputList) > 0:
            result += '\n'
            result += '\n'.join([str(l[0]) for l in outputList])
        return result