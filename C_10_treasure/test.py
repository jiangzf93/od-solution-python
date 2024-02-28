from solution import Solution

cases = [
    [0, '40 40 18', 1484],
    [1, '5 4 7', 20],
]

for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if result != case[2]:
        print('Case ' + str(c) + ' not passed, output:' + str(result))