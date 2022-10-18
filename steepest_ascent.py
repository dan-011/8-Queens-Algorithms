'''
Take a random state of the board, look at all of the possible cells for a queen,
choose the one with the lowest number of attacking queens. Continue this for each
queen until a goal state is achieved or we plateau
'''
from chess_board import *

def steepest_ascent():
    board = ChessBoard() # initialize a board
    board.random_init() # randomly scatter queens on the board
    total = 0
    successes = 0
    total_moves = 0
    moves = 0
    trial = 0
    while(total < 10000): # for 10,000 boards
        current_numAttackingQueens = board.totalAttackingQueens() # calculate the number of attacking queens of the current board
        if(current_numAttackingQueens == 0): # if the current number of attacking queens is 0, then the board is a solution, so count it and continue
            successes += 1
            total += 1
            total_moves += moves
            moves = 0
            trial = 0
            board.random_init()
            continue
        s = set()
        vals = set()
        for col in range(8): # for each column
            for row in range(8): # for each row
                _board = ChessBoard()
                _board.state = board.getState().copy() # initialize a new board with the same state as the current board
                _board[col] = row # set the queen at column 'col' to row 'row'
                numAttackingQueens = _board.totalAttackingQueens() # calculate the number of attacking queens of the new board
                s.add((numAttackingQueens, _board)) # add the new board to the set with its number of attacking queens
                vals.add(numAttackingQueens) # add the number of attacking queens to a set
        minimum_attacking_queens = min(vals) # find the minimum number of attacking queens
        minimum_boards = []
        for b in s: # create a list of the boards that have the minimum number of attacking queens
            if(minimum_attacking_queens == b[0]):
                minimum_boards.append(b)
        board = random.choice(minimum_boards)[1] # randomly set board to one of the boards with the minimum number of attacking queens, this is still approaching a local goal state since all of the boards in minimum_boards have the same number of attacking queens
        moves += 1
        trial += 1
        if(board.testBoard()): # if the board is a goal state, count the success and generate a new board
            successes += 1
            total += 1
            total_moves += moves
            moves = 0
            trial = 0
            board.random_init()
        if(board.totalAttackingQueens() == current_numAttackingQueens): # if the number of attacking queens of the new board matches that of the old board, we have hit a plateau, so count this as a failure and generate a new board
            total += 1
            board.random_init()
            moves = 0
            trial = 0
    print("Average number of successful moves: " + str(total_moves/successes))
    print("Success rate: " + str(100*(successes/10000)) + '%')


def steepest_ascent1():
    board = ChessBoard() #initialize a board
    board.random_init() # randomly scatter the queens
    trial = 0
    col = 0
    moves = 0
    total = 0
    successes = 0
    total_moves = 0
    same_pos = 0
    prev = []
    while(total < 10000): # for 10,000 boards
        trial += 1
        if(col >= 8):
            col = 0
        s = set()
        for row in range(8): # for each potential row for a queen at the current column, add the number of attacking queens and the row to the set
            board[col] = row
            # put the tuple of (numAttackingQueens, row) in the set
            s.add((board.checkNumAttackingQueens(col), row))
        lowest_val = min(s)[0] # select the lowest number of attacking queens in the set
        l = []
        for item in s: # append to l the row with the lowest number of attacking queens
            if(item[0] == lowest_val):
                l.append(item[1])
        sub_optimal_row = random.choice(l) # randomply choose one of the rows
        board[col] = sub_optimal_row # set the queen at col to the sub optimal row
        col += 1
        moves += 1
        if(board.testBoard()): # if the board is the goal state, track a success and generate a new random board
            #board.printBoard()
            total += 1
            successes += 1
            board.random_init()
            trial = 0
            total_moves += moves
            moves = 0
        if(prev == board.getState()): # if the current state matches the previous state, increment same_pos
            same_pos += 1
        if(trial == 100): # if we have been at the same state for 10 iterations (we've plateaued), or we have performed 100 trials with no successes, count a failure and generate a new board
            board.random_init()
            total += 1
            trial = 0
            moves = 0
            same_pos = 0
    print("Average number of successful moves: " + str(total_moves//successes))
    print("Success rate: " + str(100*(successes/10000)) + '%')

def steepest_ascent2():
    board = ChessBoard()
    board.random_init()
    trial = 0
    col = 0
    moves = 0
    total = 0
    successes = 0
    prev = []
    while(total < 10000):
        trial += 1
        if(col >= 8):
            col = 0
        s = set()
        for row in range(8):
            board[col] = row
            # put the tuple of (numAttackingQueens, row) in the set
            s.add((board.totalAttackingQueens(), row))
        lowest_val = min(s)[0]
        l = []
        for item in s:
            if(item[0] == lowest_val):
                l.append(item[1])
        sub_optimal_row = random.choice(l)
        board[col] = sub_optimal_row
        col += 1
        moves += 1
        if(board.testBoard()):
            #board.printBoard()
            total += 1
            successes += 1
            board.random_init()
            trial = 0
        #elif(board.getState() == prev):
        elif(trial == 100):
            board.random_init()
            total += 1
            trial = 0
        
        prev = board.getState().copy()
    print("Number of moves: " + str(moves))
    print("Success rate: " + str(100*(successes/10000)) + '%')

if __name__ == '__main__':
    steepest_ascent()