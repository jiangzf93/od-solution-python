class Solution(object):
    def solve(self, inputStr):
        inputLines = inputStr.split('\n')
        itemCount = int(inputLines[0])
        items = [int(i) for i in inputLines[1].split()[:itemCount]]
        item1, item2, item3 = sorted(items)[-3:]
        result = []
        if item1 == item2 and item2 == item3:
            result = [0]
        elif item1 == item2:
            result = [item3 - item1]
        elif item2 == item3:
            result = [item2-item1, item3-item1]
        else:
            result = [abs(item3 + item1 - 2 * item2)]
        return ' '.join([str(r) for r in result])