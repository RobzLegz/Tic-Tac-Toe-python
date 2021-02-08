board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def handle_turn():
    position = input("Choose a position from 1 to 9:")


def play_game():
    display_board()
    handle_turn()


play_game()
