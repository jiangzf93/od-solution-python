from solution import Solution

cases = [
    [0, 'CA3385,CZ6678,SC6508,DU7523,HK4456,MK0987', 'CA3385,CZ6678,DU7523,HK4456,MK0987,SC6508'],
    [1, 'MU1087,CA9908,3U0045,FM1703', '3U0045,CA9908,FM1703,MU1087'],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))