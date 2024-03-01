from solution import Solution

cases = [
    [0, """abc1 A
xyz B""", 'abc1'],
    [1, """abc1 A
xyz A""", 'NULL'],
    [2, """abc1 A
def A
alic A
xyz B""", """abc1
alic
def"""],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))