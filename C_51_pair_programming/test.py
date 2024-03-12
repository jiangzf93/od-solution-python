from solution import Solution

cases = [
    [0, """4
1 2 3 4""", 4],
    [1, """3
5 4 7""", 0],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))