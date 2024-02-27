from solution import Solution

cases = [
    [0, '3 15 6 14', '3 21 9 17'],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    if sol.solve(case[1]) != case[2]:
        unpassed.append(str(case[0]))

if unpassed:
    print('unpassed cases:' + ' '.join(unpassed))
else:
    print('all passed')