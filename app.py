board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
game_still_going = True

winner = None

current_player = "X"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def handle_turn(current_player):
    position = input("Choose a position from 1 to 9:")
    position = int(position) - 1
    board[position] = "X"
    display_board()


def check_if_game_over():
    checkIfWin()
    checkIfTie()


def checkIfWin():

    global winner

    rowWinner = checkRows()
    columnWinner = checkColumns()
    diagonalWinner = checkDiagonals()

    if rowWinner:
        # win
        winner = rowWinner
    elif columnWinner:
        # win

        winner = columnWinner
    elif diagonalWinner:
        # ein
        winner = diagonalWinner
    else:
        winner = None
    return


def checkRows():
    global game_still_going

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row1:
        return board[3]
    elif row1:
        return board[6]
    return


def checkColumns():
    return


def checkDiagonals():
    return


def checkIfTie():
    return


def flip_player():
    return


def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + "won.")
    elif winner == None:
        print("Tie.")


play_game()
