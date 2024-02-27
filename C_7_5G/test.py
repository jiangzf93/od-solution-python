from solution import Solution

cases = [
    [0, """3
3
1 2 3 0
1 3 1 0
2 3 5 0""", 4],
    [1, """3
1
1 2 5 0""", -1],
    [2, """3
3
1 2 3 0
1 3 1 0
2 3 5 1""", 1],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    if sol.solve(case[1]) != case[2]:
        unpassed.append(str(c))

if unpassed:
    print('unpassed cases:' + ' '.join(unpassed))
else:
    print('all passed')