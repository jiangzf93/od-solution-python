class Solution(object):
    def solve(self, inputStr):
        inputNum = int(inputStr)
        buffer = [i for i in range(inputNum+1)]
        pieces = [[i] for i in range(inputNum+1)]
        for n in range(2, inputNum+1):
            for s in range(1, n):
                tempBuf = buffer[s] * buffer[n - s]
                tempPiece = sorted(pieces[s] + pieces[n - s])
                if tempBuf > buffer[n]:
                    buffer[n] = tempBuf
                    pieces[n] = tempPiece
                elif tempBuf == buffer[n]:
                    if len(tempPiece) < len(pieces[n]):
                        pieces[n] = tempPiece
        return ' '.join([str(n) for n in pieces[inputNum]])