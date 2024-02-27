class Solution(object):
    def solve(self, str):
        realStr = ''
        for s in str:
            if s == '<':
                realStr = realStr[:-1]
            else:
                realStr += s
        if len(realStr) < 8:
            return realStr + ',false'
        hasUpper = False
        hasLower = False
        hasDigit = False
        hasOther = False
        for s in realStr:
            if s.isupper():
                hasUpper = True
            elif s.islower():
                hasLower = True
            elif s.isdigit():
                hasDigit = True
            else:
                hasOther = True
        if hasUpper and hasLower and hasDigit and hasOther:
            return realStr + ',true'
        else:
            return realStr + ',false'