'''
do stochastic but only move to a new location if it improves your current state

DOES THIS ALSO INCLUDE A PROBABILITY
'''

from chess_board import *

def first_choice():
    board = ChessBoard() # initialize a chess board
    board.random_init() # randomly scatter queens across the board
    total = 0
    successes = 0
    total_moves = 0
    moves = 0
    while(total < 10000):
        current_numAttackingQueens = board.totalAttackingQueens() # calculate the total attacking queens of the current board
        if(current_numAttackingQueens == 0): # if the beginning state is the goal state, count the success and generate a new random board
            successes += 1
            total += 1
            total_moves += moves
            moves = 0
            board.random_init()
            continue
        
        for col in range(8): # for each column
            for row in range(8): # for each row
                _board = ChessBoard()
                _board.state = board.getState().copy() # generate a new board with the same state of the current board
                _board[col] = row # set the queen at column 'col' to row 'row'
                numAttackingQueens = _board.totalAttackingQueens() # calculate the number of attacking queens of the new board
                if(numAttackingQueens < current_numAttackingQueens): # if the number of attacking queens is less than the old board, set the old board to the new board
                    board = _board
                    break
        moves += 1
        if(board.testBoard()): # if the board is a solution, count the success and generate a new board
            successes += 1
            total += 1
            total_moves += moves
            moves = 0
            board.random_init()
        if(board.totalAttackingQueens() == current_numAttackingQueens): # if the new board has the same number of attacking queens as the old board, we have plateaued, so consider this a failure and generate a new board
            total += 1
            board.random_init()
            moves = 0
    print("Average number of successful moves: " + str(total_moves//successes))
    print("Success rate: " + str(100*(successes/10000)) + '%')

def first_choiceBAD():
    board = ChessBoard() # initialize a chess board
    board.random_init() # randomly scatter the queens on the board
    iter = 0
    col = 0
    moves = 0
    total = 0
    successes = 0
    prev = []
    total_moves = 0
    trial = 0
    while(total < 10000): # for 10,000 chess boards
        if(col >= 8):
            col = 0
        current_state = board.checkNumAttackingQueens(col) # get the number of queens attacking the current position
        current_row = board[col]
        probabilities = []
        rows = []
        attackingQueens = []
        for row in range(8): # for each potential row, calculate the number of queens attacking the queen piece ** the number of queens attacking the current queen (this will serve as our weight/probability)
            #if(row == current_row): continue # don't add the current row 

            board[col] = row
            numAttackingQueens = board.checkNumAttackingQueens(col)
            if(numAttackingQueens > current_state): continue # ignore states that are worse than the current state
            rows.append(row)
            attackingQueens.append(numAttackingQueens)
            probabilities.append((9-numAttackingQueens)**2)
        random_row_choice = random.choices(rows, weights = probabilities)[0] # choose a row randomly based on the calculated weights
        index = rows.index(random_row_choice)
        board[col] = random_row_choice
        
        col += 1
        moves += 1
        if(board.testBoard()): # if the board results in a goal state, count the success and generate a new board
            #board.printBoard()
            total += 1
            successes += 1
            trial = 0
            board.random_init()
            total_moves += moves
            moves = 0
        elif(trial == 100): # if we have not reached a goal state in 100 trials, consider it a failure and generate a new state
            board.random_init()
            total += 1
            trial = 0
            moves = 0
        trial += 1
        
        prev = board.getState().copy()
    print("Average number of successful moves: " + str(total_moves//successes))
    print("Success rate: " + str(100*(successes/10000)) + '%')

def first_choice2():
    board = ChessBoard()
    board.random_init()
    iter = 0
    col = 0
    moves = 0
    total = 0
    successes = 0
    prev = []
    total_moves = 0
    trial = 0
    while(total < 10000):
        if(col >= 8):
            col = 0
        current_state = board.checkNumAttackingQueens(col)
        probabilities = []
        rows = []
        for row in range(8):
            board[col] = row
            # put the tuple of (numAttackingQueens, row) in the set
            numAttackingQueens = board.totalAttackingQueens()
            rows.append(row)
            probabilities.append((9-numAttackingQueens)**(9 - numAttackingQueens))
        while(len(rows) > 0):
            random_row_choice = random.choices(rows, weights = probabilities)[0]
            index = rows.index(random_row_choice)
            if(probabilities[index] >= current_state):
                board[col] = random_row_choice
                break
            else:
                del rows[index]
                del probabilities[index]
        col += 1
        moves += 1
        if(board.testBoard()):
            #board.printBoard()
            total += 1
            successes += 1
            trial = 0
            board.random_init()
            total_moves += moves
            moves = 0
        elif(trial == 100):
            board.random_init()
            total += 1
            trial = 0
            moves = 0
        trial += 1
        
        prev = board.getState().copy()
    print("Average number of successful moves: " + str(total_moves//successes))
    print("Success rate: " + str(100*(successes/10000)) + '%')
if __name__ == '__main__':
    first_choice()
    #first_choice2()