from solution import Solution

cases = [
    [0, """2 2
1 2
4 3""", 3],
    [1, """3 3
1 2 4
3 5 7
6 8 9""", 4],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if result != case[2]:
        print('Case ' + str(c) + ' not passed, output:' + result)