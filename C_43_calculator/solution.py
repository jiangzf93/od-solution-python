class fraction(object):
    def __init__(self, num):
        self.numerator = num
        self.denominator = 1

    def getGcd(self, left, right):
        if left < right:
            right, left = left, right
        if left % right == 0:
            return right
        return self.getGcd(right, left%right)
    
    def format(self, denominator, numerator):
        if numerator == 0:
            self.numerator = 0
            self.denominator = 1
            return
        if denominator < 0:
            denominator = -denominator
            numerator = -numerator
        gcd = self.getGcd(abs(denominator), abs(numerator))
        self.denominator = denominator / gcd
        self.numerator =  numerator / gcd

    def add(self, other):
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.format(denominator, numerator)
        
    def sub(self, other):
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.format(denominator, numerator)

        
    def mult(self, other):
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.numerator
        self.format(denominator, numerator)

        
    def divide(self, other):
        denominator = self.denominator * other.numerator
        numerator = self.numerator * other.denominator
        self.format(denominator, numerator)

    def getExpr(self):
        return str(int(self.numerator)) + (('/' + str(int(self.denominator))) if self.denominator != 1 else '')

class Solution(object):
    def sumFraction(self, nums):
        result = nums[0]
        for i in range(1, len(nums)):
            result.add(nums[i])
        return result

    def parseExp(self):
        sign = '+'
        num = fraction(0)
        stack = []
        while self.expr:
            c = self.expr.pop(0)
            if c.isdigit():
                num.mult(fraction(10))
                num.add(fraction(int(c)))
            elif c == '(':
                num = self.parseExp()
            if not c.isdigit() or not self.expr:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    num.mult(fraction(-1))
                    stack.append(num)
                elif sign == '*':
                    stack[-1].mult(num)
                elif sign == '/':
                    stack[-1].divide(num)
                if c == ')':
                    return self.sumFraction(stack)
                sign = c
                num = fraction(0)
        return self.sumFraction(stack)


    def solve(self, inputStr):
        self.expr = list(''.join(inputStr.split()))
        return self.parseExp().getExpr()