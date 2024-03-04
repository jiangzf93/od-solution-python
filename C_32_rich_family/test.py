from solution import Solution

cases = [
    [0, """4
100 200 300 500
1 2
1 3
2 4""", 700],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))