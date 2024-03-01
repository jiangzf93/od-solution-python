class Solution(object):
    def solve(self, inputStr):
        stat = {}
        for line in inputStr.split('\n'):
            player, shape = line.split()
            if shape in stat:
                stat[shape].append(player)
            else:
                stat[shape] = [player]
        if len(stat.keys()) != 2:
            return 'NULL'
        winPlayers = None
        if 'A' not in stat:
            winPlayers = stat['B']
        elif 'B' not in stat:
            winPlayers = stat['C']
        else:
            winPlayers = stat['A']
        return '\n'.join(sorted(winPlayers))