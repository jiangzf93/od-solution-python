from solution import Solution

cases = [
    [0, '10001', 1],
    [1, '0101', 0]
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