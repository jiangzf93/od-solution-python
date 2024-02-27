import solution

cases = [
    [
"""5
1 90
2 91
3 95
4 96
5 100""", 
"""1 2
3 4"""
    ], [
"""5
1 90
2 91
3 92
4 85
5 86""",
"""1 2
2 3
4 5"""
    ], [
"""6
1 90
2 91
3 92
4 85
5 86
6 86""",
"""5 6"""
    ], [
"""6
1 90
2 91
3 91
4 85
5 86
6 86""",
"""2 3
5 6"""
    ],
]

errorList = []
for c in range(len(cases)):
    case = cases[c]
    sol = solution.Solution()
    if sol.solve(case[0]) != case[1]:
        errorList.append(str(c))
if len(errorList) > 0:
    print('error numbers:' + ' '.join(errorList))
else:
    print('test succeed')