from solution import Solution

cases = [
    [0, 'alolobo', 6],
    [1, 'looxdolx', 7],
    [2, 'bcbcbc', 6],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))