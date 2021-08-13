"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None
number_of_steps=[0]
defensive_test=[True]


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
    number_of_x=0
    number_of_o=0
    for row in board:
        for column in row:
            if (column == X):
                number_of_x +=1
            elif (column == O):
                number_of_o +=1
    if (number_of_x>number_of_o):
        return O
    else:
        return X

        


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_positions = []
    a=0
    for row in board:
        b=0
        for column in row:
            if (column==EMPTY):
                empty_positions.append((a,b))
            b+=1
        a+=1
    empty_positions=set(empty_positions)
    
    return empty_positions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    result_board=copy.deepcopy(board)
    if (result_board[action[0]][action[1]]!=EMPTY):
        raise NotImplementedError
    else:    
        if (player(board)==X):
            result_board[action[0]][action[1]]=X
        else:
            result_board[action[0]][action[1]]=O

    return result_board

    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_player=None
    for x in range(0,3):
        if (board[x][0]==board[x][1]) and (board[x][0]==board[x][2]):
            winning_player=board[x][0]

    for y in range(0,3):
        if (board[0][y]==board[1][y]) and (board[0][y]==board[2][y]):
            winning_player=board[0][y]

    if ((board[0][0]==board[1][1]) and (board[0][0]==board[2][2])) or ((board[0][2]==board[1][1]) and (board[0][2]==board[2][0])):
        winning_player=board[1][1]

    return winning_player


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board)!=None):
        return True
    
    for x in range(0,3):
        for y in range(0,3):
            if (board[x][y]==EMPTY):
                return False

    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if (winner(board)==X):
        return 1
    elif (winner(board)==O):
        return -1
    else:
        return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    else:
        impact=-100
        if (number_of_steps[0]>9):
            number_of_steps[0]=0
        number_of_steps[0]=number_of_steps[0]+1
        for action in actions(board):
            impact=max(impact, min_value(result(board,action)))
        return impact 

def min_value(board):
    if terminal(board):
        return utility(board)
    else:
        impact=100
        if (number_of_steps[0]>9):
            number_of_steps[0]=0
        number_of_steps[0]=number_of_steps[0]+1
        for action in actions(board):
            impact=min(impact, max_value(result(board,action)))
        return impact
    
def offensive_action(board):
    """
    Determines which is the best position to play in to win the game
    """
    if (player(board)==X):
        test_base=-100
        test_base2=200
        for action in actions(board):
            number_of_steps[0]=0
            value=max_value(result(board,action))
            if (value>test_base):
                optimum_action=action
                test_base=value
                test_base2=number_of_steps[0]
            elif (value==test_base) and (number_of_steps[0]<test_base2):
                optimum_action=action
                test_base=value
                test_base2=number_of_steps[0]
    else:
        test_base=100
        test_base2=200
        for action in actions(board):
            number_of_steps[0]=0
            value=min_value(result(board,action))
            if (value<test_base):
                optimum_action=action
                test_base=value
                test_base2=number_of_steps[0]
            elif (value==test_base) and (number_of_steps[0]<test_base2):
                optimum_action=action
                test_base=value
                test_base2=number_of_steps[0]
    return optimum_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #To help reduce time for initial X action if player chooses O
    
    empty_cells=0
    for yq in board:
        for xq in yq:
            if (xq==EMPTY):
                empty_cells+=1
    if (empty_cells==9):
        random_list=[(0,1),(2,2),(1,0)]
        return random_list[random.randint(0,2)]
    
    #Actual decision making part
    for action in actions(board):
        result_board=result(board,action)
        if (terminal(result_board)): #solves problem of it hanging when you play as O and the comp reaches the last playable move 
            return offensive_action(board)
        defensive_action=offensive_action(result_board)
        if (terminal(result(result_board,defensive_action))):
            return defensive_action
    return offensive_action(board)

    
        
    





