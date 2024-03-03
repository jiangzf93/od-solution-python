from solution import Solution

cases = [
    [0, """5
/huawei/computing/no/one
/huawei/computing
/huawei
/huawei/cloud/no/one
/huawei/wireless/no/one
2 computing""", 2],
    [1, """5
/huawei/computing/no/one
/huawei/computing
/huawei
/huawei/cloud/no/one
/huawei/wireless/no/one
4 two""", 0],
]

unpassed = []
for c in range(len(cases)):
    case = cases[c]
    sol = Solution()
    result = sol.solve(case[1])
    if str(result) != str(case[2]):
        print('Case ' + str(c) + ' not passed, output:' + str(result))