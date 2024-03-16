from solution import Solution

cases = [
    [0, """3 4 2
1 5 6 6
8 3 4 3
6 8 6 3""", 3],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))