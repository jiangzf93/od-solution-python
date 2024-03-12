from solution import Solution

cases = [
    [0, '0 9 20 -1 -1 15 7 -1 -1 -1 -1 3 2', 38],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))