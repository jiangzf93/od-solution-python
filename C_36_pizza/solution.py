class Solution(object):
    def getTotalSize(self, left, right):
        leftSize, rightSize = self.pizzas[left], self.pizzas[right]
        nextOneLeft, nextOneRight = (left-1)%self.pizzaCount, (right+1)%self.pizzaCount
        nextTwoLeft, nextTwoRight = (left-2)%self.pizzaCount, (right+2)%self.pizzaCount
        if (left - right) % self.pizzaCount == 1:
            return min(leftSize, rightSize)
        if leftSize > rightSize:
            return max(self.getTotalSize(nextTwoLeft, right) + self.pizzas[nextOneLeft],
                       self.getTotalSize(nextOneLeft, nextOneRight) + rightSize)
        if leftSize < rightSize:
            return max(self.getTotalSize(nextOneLeft, nextOneRight) + leftSize,
                       self.getTotalSize(left, nextTwoRight) + self.pizzas[nextOneRight])

    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        self.pizzaCount = int(inputLines[0])
        self.pizzas = [int(p) for p in inputLines[1:self.pizzaCount+1]]
        maxSize = 0
        for p in range(len(self.pizzas)):
            maxSize = max(maxSize, self.pizzas[p] + self.getTotalSize((p-1)%self.pizzaCount, (p+1)%self.pizzaCount))
        return maxSize