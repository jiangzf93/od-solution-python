from solution import Solution

cases = [
    [0, """3 2
yuwen shuxue
fangfang 95 90
xiaohua 88 95
minmin 100 82
shuxue""", 'xiaohua fangfang minmin'],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))