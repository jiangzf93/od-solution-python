from solution import Solution

cases = [
    [0, """5
5 15 40 30 10""", '40 100 30 60 15 30 5 15 10'],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))