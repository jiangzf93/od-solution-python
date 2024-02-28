from solution import Solution

cases = [
    [0, """2
1
-5 1""", 0],
    [1, """5
-5
-5 1 6 0 -7""", 1],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))