from solution import Solution

cases = [
    [0, '10 8 36 15 7', 44],
    [1, '1 1 2 1 1', 2],
]

for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if result != case[2]:
        print('Case ' + str(c) + ' not passed, output:' + str(result))