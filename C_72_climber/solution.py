from collections import defaultdict
class Solution(object):
    def solve(self, inputStr):
        hills, health = eval(inputStr)
        linkInfo = defaultdict(dict)
        lands = []
        index = 0
        while index < len(hills):
            if hills[index] == 0:
                lands.append(index)
            landIndex = index
            while index < len(hills) - 1 and hills[index+1] >= hills[index]:
                index += 1
            hillIndex = index
            if landIndex != hillIndex:
                height = hills[hillIndex] - hills[landIndex]
                linkInfo[landIndex][hillIndex] = 2 * height
                linkInfo[hillIndex][landIndex] = height
            while index < len(hills) - 1 and hills[index+1] <= hills[index]:
                index += 1
            landIndex = index
            if landIndex != hillIndex:
                height = hills[hillIndex] - hills[landIndex]
                linkInfo[landIndex][hillIndex] = 2 * height
                linkInfo[hillIndex][landIndex] = height
        print(linkInfo)

        return 