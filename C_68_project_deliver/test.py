from solution import Solution

cases = [
    [0, """6 2 7 7 9 3 2 1 3 11 4
2""", 28],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))