from chess_board import *

def random_restart():
    board = ChessBoard() # initialize a new board
    board.random_init() # randomly scatter queens on the board
    total = 0
    successes = 0
    total_moves = 0
    moves = 0
    while(total < 10000):
        current_numAttackingQueens = board.totalAttackingQueens() # calculate the current number of attacking queens
        if(current_numAttackingQueens == 0): # if the number of attacking queens is 0, then we have found a solution, count the success and generate a new board
            successes += 1
            total += 1
            total_moves += moves
            moves = 0
            board.random_init()
            continue
        s = set()
        vals = set()
        for col in range(8): # for each column
            for row in range(8): # for each row
                _board = ChessBoard()
                _board.state = board.getState().copy() # initialize a new board with the same state as the current board
                _board[col] = row # set the queen at column 'col' to row 'row'
                numAttackingQueens = _board.totalAttackingQueens() # calculate the number of attacking queens
                s.add((numAttackingQueens, _board)) # add the new board to the set s with its number of attacking queens
                vals.add(numAttackingQueens) # add the number of attacking queens to the set vals
        minimum_attacking_queens = min(vals) # find the minimum number of attacking queens from all the states
        minimum_boards = []
        for b in s: # populate minimum_boards with the boards with the minimum number of attacking queens
            if(minimum_attacking_queens == b[0]):
                minimum_boards.append(b)
        board = random.choice(minimum_boards)[1] # randomly choose from minimum_boards, this still satisfies finding a local minimum since all of the boards in minimum_boards have the same number of attacking queens
        moves += 1
        if(board.testBoard()): # if the board is a solution, count the success and generate a new board
            successes += 1
            total += 1
            total_moves += moves
            moves = 0
            board.random_init()
        if(board.totalAttackingQueens() == current_numAttackingQueens): # if the number of attacking queens of our old board is the same as that of our new board, we hav plateaued, so randomly restart at a new board state
            board.random_init()
    print("Average number of successful moves: " + str(total_moves//successes))
    print("Success rate: " + str(100*(successes/10000)) + '%')

def random_restart1():
    board = ChessBoard() # initialize a board
    board.random_init() # randomly scatter
    trial = 0
    col = 0
    moves = 0
    total_moves = 0
    total = 0
    successes = 0
    total_moves = 0
    prev = []
    while(total < 10000): # for 10,000 boards, do the following
        if(col >= 8): 
            col = 0
        if(prev == board.getState()): # if the previous state matches the current state, we have plateaued, so randomly restart at another state
            trial += 1
            board.random_init()
        prev = board.getState().copy() # copy the current board state to serve as the previous board

        s = set()
        for row in range(8):
            board[col] = row
            s.add((board.checkNumAttackingQueens(col), row)) # for each potential row at the current column, store into a set the number of attacking queens at that row and the row
        lowest_val = min(s)[0] # find the minimum number of attacking queens in the set
        l = []
        for item in s: # for each item in the set, append the row that have the minimum number of attacking queens
            if(item[0] == lowest_val):
                l.append(item[1])
        sub_optimal_row = random.choice(l) # randomly select one of the rows
        '''
        LOOK HERE
        '''
        board[col] = sub_optimal_row # set the queen at the current column to the sub-optimal row
        # board[col] = min(s)[1]
        col += 1 # increment the current column
        moves += 1
        if(board.testBoard()): # if the board is a solution state, then increment our successes and generate a new random board
            #board.printBoard()
            total += 1
            successes += 1
            board.random_init()
            trial = 0
            total_moves += moves
            moves = 0
        #elif(board.getState() == prev):
        if(trial == 100): # if we have gone through 100 trials with the same board and still have not found a solution, consider it a failure and generate a new random board state
            board.random_init()
            total += 1
            trial = 0
            moves = 0
        
    print("Average number of successful moves: " + str(total_moves//successes))
    print("Success rate: " + str(100*(successes/10000)) + '%')

def random_restart2():
    board = ChessBoard()
    board.random_init()
    trial = 0
    col = 0
    moves = 0
    total_moves = 0
    total = 0
    successes = 0
    total_moves = 0
    prev = []
    while(total < 10000):
        if(col >= 8):
            board.random_init()
            col = 0
            trial += 1
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
            total_moves += moves
            moves = 0
        #elif(board.getState() == prev):
        if(trial == 100):
            board.random_init()
            total += 1
            trial = 0
            moves = 0
        
        prev = board.getState().copy()
    print("Average number of successful moves: " + str(total_moves//successes))
    print("Success rate: " + str(100*(successes/10000)) + '%')

def random_restartold():
    board = ChessBoard()
    board.random_init()
    iter = 0
    col = 0
    moves = 0
    while(iter < 10000):
        if(col >= 8):
            board.random_init()
            col = 0
        s = set()
        for row in range(8):
            board[col] = row
            # put the tuple of (numAttackingQueens, row) in the set
            s.add((board.checkNumAttackingQueens(col), row))
        sub_optimal_row = min(s)[1]
        board[col] = sub_optimal_row
        col += 1
        iter += 1
    print("Number of moves: " + str(iter))
    board.printBoard()

if __name__ == '__main__':
    random_restart()