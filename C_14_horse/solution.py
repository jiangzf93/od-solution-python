class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        inputDim = inputLines[0].split()
        rows = int(inputDim[0])
        cols = int(inputDim[1])
        matrix = [[int(c) for c in r[:cols]] for r in inputLines[1:rows+1]]
        
        return False