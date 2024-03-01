from solution import Solution

cases = [
    [0, """4
cat
bt
hat
tree
atach??""", 3],
    [1, """3
hello
world
cloud
welldonehohneyr""", 2],
    [2, """3
apple
car
window
welldoneapplec?""", 2],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))