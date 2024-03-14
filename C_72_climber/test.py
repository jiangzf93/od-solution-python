from solution import Solution

cases = [
    [0, '[0,1,4,3,1,0,0,1,2,3,1,2,1,0],13', 3],
    [1, '[1,4,3],999', 0],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))