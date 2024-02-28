from solution import Solution

cases = [
    [0, """2 2
1 1
2 2""", '1 2'],
    [1, """2 2
1 2
2 3""", '1 2'],
    [2, """1 2
2
1 3""", '2 3'],
    [3, """3 2
1 2 5
2 4""", '5 4'],
]

for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if result != case[2]:
        print('Case ' + str(c) + ' not passed, output:' + str(result))