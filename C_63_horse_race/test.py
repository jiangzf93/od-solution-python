from solution import Solution

cases = [
    [0, """11 8 20
10 13 7""", 1],
    [1, """11 12 20
10 13 7""", 2],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))