from chess_board import *
from stack import *
import random

'''
FIX TO HAVE EMPTY BOARD
'''

def dfs():
    board = ChessBoard() # create a board
    stack = Stack() # initialize a stack
    #board.clear_board() # clear the board (no queens at the beginning)
    board[0] = 0 # place the first queen at column 0 in row 0
    stack.push(((board[0], 0), board.getState().copy())) # push onto the stack the queen's row,col position and the board state
    hasPopped = False
    moves = 1
    while(not(board.testBoard())): # while the board is not a solution and the stack isn't empty
        prev_config = stack.peek() # get the previous state of the board
        prev_col = prev_config[0][1]
        prev_state = prev_config[1]
        board.setBoard(prev_state) # set the board to the previous state

        new_col = prev_col + 1 # change the position of the queen in the next column
        if(new_col == 8):
            if(board.testBoard()):
                break
            else:
                stack.pop()
                continue
        while(hasPopped or (not(board.testBoardFrom(new_col)) and board[new_col] < 8)): # find the row where the queen is not being attacked by any other queens
            board[new_col] +=1
            hasPopped = False
        if(board[new_col] < 8): # if a position was found, push it onto the stack
            stack.push(((board[new_col], new_col), board.getState().copy()))
            moves += 1
            hasPopped = False
        elif(board[new_col] == 8): # if there was no position such that the queen would create a state with a valid solution, pop the state from the stack
            stack.pop()
            hasPopped = True
    assert(board.testBoard())
    print("Boards Generated: " + str(moves))
    board.printBoard() # print the board

if __name__ == '__main__':
    dfs()