class Solution(object):
    def solve(self, inputStr):
        inputNums = inputStr.split()
        rows = int(inputNums[0])
        cols = int(inputNums[1])
        target = int(inputNums[2])
        result = 0
        for r in range(rows):
            for c in range(cols):
                bitSum = r // 10 + r % 10 + c // 10 + c % 10
                if bitSum <= target:
                    result += 1
        print(result)
        return result