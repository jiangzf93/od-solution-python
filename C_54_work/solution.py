class Solution(object):

    def getDays(self, tasks, num):
        days = 0
        left, right = 0 ,len(tasks)-1
        while left < right:
            if tasks[left] + tasks[right] <= num:
                left += 1
                right -= 1
            else:
                right -= 1
            days += 1
        if left == right:
            days += 1
        return days


    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        months = int(inputLines[0])
        tasks = sorted([int(p) for p in inputLines[1].split()])
        left, right = max(tasks), sum(tasks)
        while left <= right:
            mid = (left + right) // 2
            days = self.getDays(tasks, mid)
            if days == months:
                right = mid - 1
            elif days > months:
                left = mid + 1
            else:
                right = mid - 1
        return left