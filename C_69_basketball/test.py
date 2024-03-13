from solution import Solution

cases = [
    [0, """4,5,6,7,0,1,2
6,4,0,1,2,5,7""", 'RLRRRLL'],
    [1, """4,5,6,7,0,1,2
6,0,5,1,2,4,7""", 'NO'],
    [2, """4,5,6,7,0,1,2
6,0,5,1,2,4,7""", 'NO'],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))