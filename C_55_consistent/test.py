from solution import Solution

cases = [
    [0, 21, '21=10+11'],
    [0, 24, '24=7+8+9'],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))
    else:
        print('Case ' + str(c) + ' passed')