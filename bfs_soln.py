from chess_board import *
from my_queue import *

'''
FIX TO HAVE EMPTY BOARD
'''

def bfs():
    board = ChessBoard() # initialize a board
    queue = MyQueue() # initialize a queue
    #board.clear_board() # clear the board (no queens)
    board[0] = 0 # place the queen at column 0 to row 0
    queue.enqueue(((board[0], 0), board.getState().copy())) # enqueue the queen's position and the current board state
    moves = 1 # number of moves that lead to a solution or number of moves in general
    while(len(queue) > 0): # while the queue is not empty
        prev_config = queue.dequeue() # dequeue the first item in the queue
        prev_col = prev_config[0][1]
        prev_state = prev_config[1]
        board.setBoard(prev_state) # set the board to the dequeued state

        if(board.testBoard()): break # test the board to see if we hav arrived to a solution
        new_col = prev_col + 1 # calculate the next column to move the queen in
        for i in range(8): # for each row
            moves += 1
            l = board.getState().copy()
            l[new_col] = i
            b1 = ChessBoard(l) # create a board with a queen at row i
            if(b1.testBoardFrom(new_col)): # if the row results in a potential solution state, enqueue the state
                queue.enqueue(((i, new_col), l))
    assert(board.testBoard())
    print("Boards Generated: " + str(moves))
    board.printBoard()

if __name__ == '__main__':
    bfs()