from solution import Solution

cases = [
    [0, """7 -2 6 6 9
6 7 -2 9 6""", '-2 0 20 0 6'],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))