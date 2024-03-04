from solution import Solution

cases = [
    [0, """5 4
1
1
2
3
5
1 2 3
1 4
3 4 5
2 3 4""", """3
4
1
2"""],
    [1, """3 3
3
1
5
1 2 3
1 2 3
1 2 3""", """1
2
3"""],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))