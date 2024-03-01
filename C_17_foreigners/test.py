from solution import Solution

cases = [
    [0, '10 2 4', 2],
    [1, '10 4 4', 0],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))