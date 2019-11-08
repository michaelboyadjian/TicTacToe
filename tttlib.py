# Tic Tac Toe

import random

def genBoard():
    emptyboard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    return emptyboard

def printBoard(T):
    position = 0
    accum = []
    if len(T) != 9:
        return False
    for element in T:
        if element == 0:
            accum = accum + [position]
        elif element == 1:
            accum = accum + ["X"]
        elif element == 2:
            accum = accum + ["O"]
        else:
            return False
        position = position + 1
    # prints board
    print(" " + str(accum[0]) + " | " + str(accum[1]) + " | " + str(accum[2]) + " ")
    print("---|---|---")
    print(" " + str(accum[3]) + " | " + str(accum[4]) + " | " + str(accum[5]) + " ")
    print("---|---|---")
    print(" " + str(accum[6]) + " | " + str(accum[7]) + " | " + str(accum[8]) + " ")
    return True


def analyzeBoard(T):
    # winning combinations of x
    if (T[0]*T[3]*T[6] == 1) or (T[1]*T[4]*T[7] == 1) or (T[2]*T[5]*T[8] == 1):
        return 1
    elif (T[0]*T[1]*T[2] == 1) or (T[3]*T[4]*T[5] == 1) or (T[6]*T[7]*T[8] == 1):
        return 1
    elif (T[0]*T[4]*T[8] == 1) or (T[6]*T[4]*T[2] == 1):
        return 1
    # winning combinations of o
    if (T[0]*T[3]*T[6] == 8) or (T[1]*T[4]*T[7] == 8) or (T[2]*T[5]*T[8] == 8):
        return 2
    elif (T[0]*T[1]*T[2] == 8) or (T[3]*T[4]*T[5] == 8) or (T[6]*T[7]*T[8] == 8):
        return 2
    elif (T[0]*T[4]*T[8] == 8) or (T[6]*T[4]*T[2] == 8):
        return 2
    # game is draw
    if T[0]*T[1]*T[2]*T[3]*T[4]*T[5]*T[6]*T[7]*T[8] == 16:
        return 3
    # error check
    for element in T:
        if element != 0 and element != 1 and element != 2:
            return (-1)
    if len(T) != 9:
        return (-1)
    if type(T) != list:
        return (-1)
    # board in play
    if (T[0] == 0) or (T[1] == 0) or (T[2] == 0) or (T[3] == 0) or (T[4] == 0) or (T[5] == 0) or (T[6] == 0) or (T[7] == 0) or (T[8] == 0):
        return 0


def genNonLoser(T, player):
    M = list(T)
    move = 0
    if player == 1:
        for element in M:
            M = list(T)
            if element == 0:
                M[move] = 2
                if analyzeBoard(M) == 2:
                    return move
                    M = list(T)
            move = move + 1
    elif player == 2:
        for element in M:
            M = list(T)
            if element == 0:
                M[move] = 1
                if analyzeBoard(M) == 1:
                    return move
                    M = list(T)
            move = move + 1
    if len(M) != 9:
        return -1
    if player != 1 or player != 2:
        return -1
    else:
        return -1


def genWinningMove(T, player):
    M = list(T)
    move = 0
    if player == 1:
        for element in M:
            M = list(T)
            if element == 0:
                M[move] = 1
                if analyzeBoard(M) == 1:
                    return move
                    M = list(T)
            move = move + 1
    elif player == 2:
        for element in M:
            M = list(T)
            if element == 0:
                M[move] = 2
                if analyzeBoard(M) == 2:
                    return move
                    M = list(T)
            move = move + 1
    if len(M) != 9:
        return -1
    if player != 1 or player != 2:
        return -1


def genRandomMove(T, player):
    M = list(T)
    I = random.randint(0,8)
    if M[I] == 0:
        return I
    else:
        return genRandomMove(T, player)
    if len(M) != 9:
        return -1
    if player != 1 or player != 2:
        return -1


def genOpenMove(T, player):
    M = list(T)
    position = 0
    for element in M:
        if element == 0:
            return position
        position = position + 1
    if len(M) != 9:
        return -1
    if player != 1 or player != 2:
        return -1



