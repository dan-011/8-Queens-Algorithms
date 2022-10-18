'''
for each cost make a list to increase the probability that higher cost moves are chosen
'''

from chess_board import *

def stochastic():
    board = ChessBoard() # initialize a chessboard
    board.random_init() # randomly scatter queens on the board
    total = 0
    successes = 0
    total_moves = 0
    moves = 0
    soln = None
    while(total < 10000): # for 10,000 boards
        current_numAttackingQueens = board.totalAttackingQueens() # find the current number of total queens attacking each other
        if(current_numAttackingQueens == 0): # if the number is 0, this is a goal state, so we can count the success and generate a new board
            successes += 1
            current_numAttackingQueens = board.totalAttackingQueens()
            total += 1
            total_moves += moves
            moves = 0
            board.random_init()
            continue
        boards = []
        probabilities = []
        for col in range(8): # for 8 columns
            for row in range(8): # for 8 rows
                _board = ChessBoard() # generate a new board
                _board.state = board.getState().copy() # set the board's state to the state of the current board
                _board[col] = row # move the queen at column 'col' to row 'row'
                numAttackingQueens = _board.totalAttackingQueens() # evaluate the number of attacking queens for this board
                if(numAttackingQueens < current_numAttackingQueens): # if the number of attacking queens is less than that of the current board
                    boards.append(_board) # append the new board to the collection of boards
                    if(numAttackingQueens == 0): # if the probability is 0, we have found a solution
                        soln = _board
                    else:
                        probabilities.append(1/numAttackingQueens) # otherwise, append 1/numAttackingQueens as a probability for this board to be randomly chosen
        if(len(boards) == 0): # no boards were found with a better state than our current board, this is a failure, so generate a new random board
            total += 1
            board.random_init()
            moves = 0
            continue
        if(soln is None): # if we didn't find a solution, set board to a random board chosen based on the calculated probabilities
            board = random.choices(boards, weights = probabilities)[0]
        else: # if we did find a solution, set the board to that solution state
            board = soln
        soln = None
        moves += 1
        if(board.testBoard()): # if the board is a solution, count the success and generate an new board
            successes += 1
            total += 1
            total_moves += moves
            moves = 0
            board.random_init()
        if(board.totalAttackingQueens() == current_numAttackingQueens): # if the number of attacking queens of the old board is the same as the number of attacking queens of the previous board, then we have plateaued, so count as a failure and generate a new board
            total += 1
            board.random_init()
            moves = 0
    print("Average number of successful moves: " + str(total_moves/successes))
    print("Success rate: " + str(100*(successes/10000)) + '%')
        


        
def stochasticBAD():
    board = ChessBoard() # generate a new chess board
    board.random_init() # ranomly scatter the queens on the board
    iter = 0
    col = 0
    moves = 0
    total = 0
    successes = 0
    prev = []
    trial = 0
    total_moves = 0
    while(total < 10000): # for 10,000 boards
        if(col >= 8):
            col = 0
        probabilities = []
        #current_row = board[col]
        rows = []
        for row in range(8): # for each of the possible rows for a current column
            board[col] = row
            numAttackingQueens = board.checkNumAttackingQueens(col) # get the number of queens attacking the current queen at that row
            rows.append(row)
            probabilities.append((9-numAttackingQueens)**(9-numAttackingQueens)) # calculate the probability/weight of the current position based on the number of attacking queens
        random_row_choice = random.choices(rows, weights = probabilities)[0] # choose a row randomly based off of the weights/probabilities
        board[col] = random_row_choice # set the queen to the randomly selected row
        col += 1
        moves += 1
        trial += 1
        if(board.testBoard()): # if the board is a goal state, count the success and generate a new random board
            total += 1
            successes += 1
            board.random_init()
            trial = 0
            total_moves += moves
            moves = 0
        elif(trial == 100): # if we have not found a goal state in 100 trials, count it a failure and generate a new random board
            board.random_init()
            total += 1
            trial = 0
            moves = 0
        
        prev = board.getState().copy()
    print("Average number of successful moves: " + str(total_moves//successes))
    print("Success rate: " + str(100*(successes/10000)) + '%')

def stochastic2():
    board = ChessBoard()
    board.random_init()
    iter = 0
    col = 0
    moves = 0
    total = 0
    successes = 0
    total_moves = 0
    prev = []
    trial = 0
    while(total < 10000):
        if(col >= 8):
            col = 0
        probabilities = []
        rows = []
        for row in range(8):
            board[col] = row
            # put the tuple of (numAttackingQueens, row) in the set
            numAttackingQueens = board.totalAttackingQueens()
            rows.append(row)
            probabilities.append((9-numAttackingQueens)**(9-numAttackingQueens))
        random_row_choice = random.choices(rows, weights = probabilities)[0]
        board[col] = random_row_choice
        col += 1
        moves += 1
        trial += 1
        if(board.testBoard()):
            #board.printBoard()
            total += 1
            successes += 1
            board.random_init()
            trial = 0
            total_moves += moves
            moves = 0
        elif(trial == 100):
            board.random_init()
            total += 1
            trial = 0
            moves = 0
        
        prev = board.getState().copy()
    print("Average number of successful moves: " + str(total_moves//successes))
    print("Success rate: " + str(100*(successes/10000)) + '%')
if __name__ == '__main__':
    stochastic()
