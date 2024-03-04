from solution import Solution

cases = [
    [0, '30 12 25 8 19', 15],
    [1, '10 12 25 8 19 8 6 4 17 19 20 30', -1],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))