from solution import Solution

cases = [
    [0, """5 100 10
10 20 30 40 50
3 4 5 6 10
20 30 20 40 30""", '0 30 0 40 0'],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))