class Solution(object):
    def solve(self, heights):
        if len(heights) <= 1:
            return 0
        else:
            result = 0
            lenH = len(heights)
            if heights[0] > heights[1]:
                result += 1
            if heights[lenH-1] > heights[lenH-2]:
                result += 1
            for i in range(1, len(heights)-1):
                if heights[i] > heights[i-1] and heights[i] > heights[i+1]:
                    result += 1
            return result