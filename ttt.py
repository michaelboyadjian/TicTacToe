from tttlib import *

T = genBoard()
while True:
    # player inputs X move
    printBoard(T)
    moveX = input("X move? ")
    # check moveX for valid input
    # if valid and if T is unoccupied at moveX, set the appropriate posiion of T via: T[int(moveX)] = 1
    if (0 <= int(moveX) < 9) and T[int(moveX)] == 0 and type(T) == list:
        T[int(moveX)] = 1
        print("Game is in progress...")
    else:
        print("Can't go there!")
        break
    state = analyzeBoard(T)
    # check if state says X won and act accordingly and break
    if state == 1:
        print("X wins!")
        break
    # check if state says draw and act accordingly and break
    if state == 3:
        print("Draw")
        break
    if state == -1:
        print("error")

    # computer inputs O move
    if genWinningMove(T, 2) != -1:
        moveO = genWinningMove(T, 2)
        print('O takes position ' + str(moveO))
    elif genNonLoser(T, 2) != -1:
        moveO = genNonLoser(T, 2)
        print('O takes position ' + str(moveO))
    elif genWinningMove(T, 2) == -1 and genNonLoser(T, 2) == -1:
        moveO = genRandomMove(T, 2)
        print('O takes position ' + str(moveO))

    T[moveO] = 2

    state = analyzeBoard(T)
    # check if state says O won and act accordingly and break
    if state == 2:
        print("O wins!")
        break
    if state == -1:
        print("error")

