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
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def checkColumns():
    global game_still_going

    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        game_still_going = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return


def checkDiagonals():
    global game_still_going

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[6] == board[4] == board[2] != "-"
    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
    elif diagonal1:
        return board[6]
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
