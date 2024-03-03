from solution import Solution

cases = [
    [0, """7
8
4
6
3
1
6
7
10""", 3],
    [1, """0
1""", 0],
    [2, """9
6
1
3
1
8
9
3
2
4
15""", 4],
    [3, """9
1
1
1
1
1
1
1
1
1
10""", 9],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))