from solution import Solution

cases = [
    [0, [[1,4],[2,5],[7,9],[14,18]], [[1,5],[7,9],[14,18]]],
    [1, [[1,4],[4,5]], [[1,5]]],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if result != case[2]:
        print('Case ' + str(c) + ' not passed, output:' + result)