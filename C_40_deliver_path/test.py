from solution import Solution

cases = [
    [0, """2 1
1 1000
2 1200
1 2 300""", 2500],
    [1, """5  1
5 1000
9 1200
17 300
132 700
500 2300
5 9 400""", 9200],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))