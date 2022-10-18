import random

class ChessBoard:
    def __init__(self, l = [0,0,0,0,0,0,0,0]):
        self.state = l

    def clear_board(self):
        for i in range(8):
            self.state[i] = -1

    def checkNumAttackingQueens(self, queen):
        count = 0
        for j in range(len(self.state)):
            distance = abs(j - queen)
            if(queen == j):
                continue
            elif(self.state[queen] == self.state[j]):
                count += 1 # at the same row
            elif (self.state[queen] == self.state[j] + distance) or (self.state[queen] == self.state[j] - distance):
                count += 1
        return count

    def totalAttackingQueens(self):
        count = 0
        for i in range(8):
            count += self.checkNumAttackingQueens(i)
        return count

    def isEmpty(self):
        for q in self.state:
            if(q > -1):
                return False
        return True

    def random_init(self):
        for i in range(len(self.state)):
            self.state[i] = random.randint(0, 7)

    def testBoard(self):
        for i in range(len(self.state)):
            for j in range(len(self.state)):
                if(i == j):
                    continue # we don't want to compare a queen to itself
                if(self.state[i] == self.state[j]):
                    return False # they are at the same row
                distance = abs(j - i)
                if (self.state[i] == self.state[j] + distance) or (self.state[i] == self.state[j] - distance):
                    return False
        for e in self.state:
            if(e == -1 or e == 8): return False
        return (True and not(self.isEmpty()))

    def testBoardFrom(self, index):
        for i in range(index):
            if(self.state[i] == self.state[index]):
                return False # they are at the same row
            distance = abs(index - i)
            if(self.state[index] == self.state[i] + distance) or (self.state[index] == self.state[i] - distance):
                return False # they are within a diagonal
        return (True and not(self.isEmpty()))

    def printBoard(self):
        for row in range(len(self.state) - 1, -1, -1):
            str = ""
            for col in range(len(self.state)):
                if(self.state[col] == row):
                    str += 'Q '
                else:
                    str += '* '
            print(str)
        print()
    
    def __getitem__(self, index):
        return self.state[index]
    
    def getState(self):
        return self.state
    
    def __setitem__(self, index, value):
        self.state[index] = value

    def moveQueen(self, col, dist):
        if(self.state[col] + dist > 7):
            raise IndexError
        self.state[col] + dist
    
    def setBoard(self, l):
        self.state = l
    
    def numAttackingQueens(self):
        res = []
        for i in range(len(self.state)):
            count = 0
            for j in range(len(self.state)):
                if(i == j):
                    continue # we don't want to compare a queen to itself
                if(self.state[i] == self.state[j]):
                    count += 1 # they are at the same row
                distance = abs(j - i)
                if (self.state[i] == self.state[j] + distance) or (self.state[i] == self.state[j] - distance):
                    count += 1
            res.append(count)
        return res
if __name__ == '__main__':
    chessF = ChessBoard([2, 7, 3, 5, 0, 6, 1, 4])
    chessT = ChessBoard([2, 7, 3, 6, 0, 5, 1, 4])

    assert(not(chessF.testBoard()))
    assert(chessT.testBoard())

    chessT.printBoard()
    chessF.printBoard()
    for i in chessT.numAttackingQueens():
        assert(i == 0)
    
    attackingQueens = chessF.numAttackingQueens()
    string = ""
    for i in attackingQueens:
        string += str(i) + ' '
    print(string)
    assert(chessF.testBoardFrom(2))
    assert(not(chessF.testBoardFrom(3)))
    
    for i in range(8):
        assert(chessF.checkNumAttackingQueens(i) == attackingQueens[i])
    
    board = ChessBoard()
    board.printBoard()
    board.clear_board()
    board.printBoard()
    board.getState()[0] = 0
    board.printBoard()