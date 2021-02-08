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
