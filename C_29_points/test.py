from solution import Solution

cases = [
    [0, """4
3
1 2
1 3
1 4
1 5""", 5],
    [1, """4
3
1 2
1 3
1 4
3 5""", 9],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))