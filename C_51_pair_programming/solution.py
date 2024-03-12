class Solution(object):
    def __init__(self):
        self.result = 0
        self.trace = []

    def backtrace(self, index):
        self.trace.append(self.persons[index])
        if len(self.trace) == 3:
            if (self.trace[0] < self.trace[1] and self.trace[1] < self.trace[2]) or \
                (self.trace[0] > self.trace[1] and self.trace[1] > self.trace[2]):
                self.result += 1
        else:
            for i in range(index+1, self.pCount):
                self.backtrace(i)
        self.trace.pop()
        return

    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        self.pCount = int(inputLines[0])
        self.persons = [int(p) for p in inputLines[1].split()[:self.pCount]]
        for i in range(self.pCount):
            self.backtrace(i)
        return self.result