from solution import Solution

cases = [
    [0, 10, 1],
    [1, 11, 3],
    [2, 12, 4],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))