from solution import Solution

cases = [
    [0, """4
8 6 2 8 6
camila 66 70 46 158 80
victoria 94 76 86 189 211
anthony 29 17 83 21 48
emily 53 97 1 19 218""", """victoria
camila
emily
anthony"""],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))