from solution import Solution

cases = [
    [0, '[[1,2,3],[4,5,6],[7,8,9]],60,0,0,2,2', 245],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))