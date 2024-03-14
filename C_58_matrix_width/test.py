from solution import Solution

cases = [
    [0, """2 5
1 2 2 3 1
2 3 2 3 2
3
1 2 3""", 2],
    [1, """2 5
1 2 2 3 1
1 3 2 3 4
3
1 1 4""", 5],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))