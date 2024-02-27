import solution

sol = solution.Solution()

assert sol.solve([0,1,2,3,2,4]) == 2
assert sol.solve([3,0,3,4,1]) == 2

assert sol.solve([]) == 0

assert sol.solve([1]) == 0

assert sol.solve([2,2,2,2,2]) == 0

assert sol.solve([1,2,3,4,5]) == 1

assert sol.solve([0,1,0,1,0]) == 2

print("All test cases passed!")