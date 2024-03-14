from solution import Solution

cases = [
    [0, """2,2
10,20
30,40""", 70],
    [1, """4,4
10,30,30,20
30,30,-1,10
0,20,20,40
10,-1,30,40""", 70],
    [2, """4,5
10,0,30,-1,10
30,0,20,0,20
10,0,10,0,30
10,-1,30,0,10""", 60],
    [3, """4,4
10,30,30,20
30,30,20,10
10,20,10,40
10,20,30,40""", -1],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))