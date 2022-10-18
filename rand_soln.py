from cgi import test
from chess_board import *
'''
def rand():
    board = ChessBoard()
    board.random_init()
    count = 1
    while(not(board.testBoard())):
        board.random_init()
        count += 1
    print("Boards Generated: " + str(count))
    board.printBoard()
'''
def rand():
    board = ChessBoard()
    board.random_init()
    count = 0
    total = 0
    successes = 0
    while(total < 1000000):
        board.random_init()
        if(board.testBoard()):
            board.printBoard()
            successes += 1
        count += 1
        total += 1
    print("Boards Generated: " + str(count))
    print("Success Rate: " + str(100*(successes/total)) + '%')

rand()