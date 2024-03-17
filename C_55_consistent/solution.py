import heapq

class Solution(object):
    def solve(self, inputNum):
        left, right = 0, 1
        addResult = 0
        start = 0
        minLength = float('inf')
        while left <= inputNum // 2 and right < inputNum: 
            addResult += right
            while left < right and addResult > inputNum:
                addResult -= left
                left += 1
            if addResult == inputNum:
                minLength = min(minLength, right - left + 1)
                start = left
            right += 1
        if start <= 0:
            return 'N'
        return str(inputNum) + '=' + '+'.join([str(start+i) for i in range(minLength)])