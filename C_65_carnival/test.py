from solution import Solution

cases = [
    [0, """5 14 30 100
1 3 5 20 21 200 202 230""", 40],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))