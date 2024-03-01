from solution import Solution

cases = [
    [0, """5
5000 2000 5000 8000 1800""", 3],
    [1, """3
5000 4000 3000""", 3]
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))