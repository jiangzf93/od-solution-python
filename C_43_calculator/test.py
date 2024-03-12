from solution import Solution

cases = [
    [0, '1 + 5 * 7 / 8', '43/8'],
    [1, '1 / (0 - 5)', '-1/5'],
    [2, '1 * (3 * 4 / (8 - (7 + 0)))', '12'],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))