"""
Tic Tac Toe Player
"""

import math
import random 
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_num = 0
    O_num = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == X:
                X_num += 1  
            elif board[i][j] == O:
                O_num += 1
    if X_num == O_num:
        return X
    else:
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    myList = []
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] is EMPTY:
                val = (i,j)   
                myList.append(val)
    return myList
        

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = board
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (
        board[0][0] == player(board) and board[0][1] == player(board) and board[0][2] == player(board) or
        board[1][0] == player(board) and board[1][1] == player(board) and board[1][2] == player(board) or
        board[2][0] == player(board) and board[2][1] == player(board) and board[2][2] == player(board) or
        
        board[0][0] == player(board) and board[1][0] == player(board) and board[2][0] == player(board) or
        board[0][1] == player(board) and board[1][1] == player(board) and board[2][1] == player(board) or
        board[0][2] == player(board) and board[1][2] == player(board) and board[2][2] == player(board) or
        
        board[0][0] == player(board) and board[1][1] == player(board) and board[2][2] == player(board) or
        board[2][0] == player(board) and board[1][1] == player(board) and board[0][2] == player(board) 
        ):
        return player(board)
    else:
        return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] is None:
                    return False
        return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is not None:
        if winner(board) == X:
            return 1
        else:
            return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    freePositions = actions(board)
    currentPlayer = player(board)
    freeLen = len(freePositions)
    if freeLen == 9:
        x_pos = 0
        y_pos = 0

        while (board[x_pos][y_pos] is not None): 
            x_pos = random.randint(0,2)
            y_pos = random.randint(0,2)
        return(x_pos,y_pos)
    
    if currentPlayer == X:
        best = [None, None, -100]
    else:
        best = [None, None, 100]
    
    if freeLen == 0 or terminal(board):
        score = utility(board)
        return [None, None, score]
    # display_board(board)
    
    
    for freeCell in freePositions:
        tmpX = freeCell[0]
        tmpY = freeCell[1]
        board[tmpX][tmpY] = currentPlayer
        result = minimax(board)
        board[tmpX][tmpY] = None
        result[0]=tmpX
        result[1]=tmpY

        if currentPlayer == X:
            if result[2] > best[2]:
                best = result #max bal
        else :
            if result[2] < best[2]:
                best = result #min val
    return best
    
            
        
    
    

    # x_pos = 0
    # y_pos = 0

    # while (board[x_pos][y_pos] is not None): 
    #     x_pos = random.randint(0,2)
    #     y_pos = random.randint(0,2)
    # return(x_pos,y_pos)




def display_board(board):
    """
    Display the current board state to console
    """
    tmpBoard = board
    for i in range(0,3):
        row = [ 0,0,0]
        for j in range(0,3):
            row[j] = tmpBoard[i][j]
        tmpBoard[i] = row
        print(tmpBoard[i])
    print("\n")


