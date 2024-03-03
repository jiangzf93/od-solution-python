from solution import Solution

cases = [
    [0, '2 8 3 7 3 6 3 5 4 4 5 3 6 2 7 3 8 4 7 5', '2 8 3 7 3 5 6 2 8 4 7 5'],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))