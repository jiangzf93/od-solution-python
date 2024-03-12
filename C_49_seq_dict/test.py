from solution import Solution

cases = [
    [0, """2
0 3
3
0 0 2
1 3 4
6 6 4 """, '0 1 1 1'],
    [1, """2
0 5
3
0 0 2
1 3 4
6 6 4 """, 'error'],
    [1, """1
3
3
0 0 2
1 3 4
6 6 4 """, '1 1'],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))