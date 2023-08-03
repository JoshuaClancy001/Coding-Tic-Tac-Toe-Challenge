import random


def user_wins():
    print('You Win')
    answer = input('Play Again? (Yes or No)')
    if answer == 'Yes' or answer == 'yes':
        wants_to_keep_playing = True
        turn_number = 1
        for i in range(2):
            for j in range(2):
                board[i][j] = '*'
    return True


def computer_wins():
    print('Computer Wins')
    answer = input('Play Again? (Yes or No)')
    if answer == 'Yes' or answer == 'yes':
        wants_to_keep_playing = True
        for i in range(2):
            for j in range(2):
                board[i][j] = '*'
    return True


def does_someone_win():
    if board[0][0] == board[0][1] == board[0][2] == 'X':
        user_wins()
    elif board[1][0] == board[1][1] == board[1][2] == 'X':
        user_wins()
    elif board[2][0] == board[2][1] == board[2][2] == 'X':
        user_wins()
    elif board[0][0] == board[1][0] == board[2][0] == 'X':
        user_wins()
    elif board[1][0] == board[1][1] == board[1][2] == 'X':
        user_wins()
    elif board[2][0] == board[2][2] == board[2][2] == 'X':
        user_wins()
    elif board[0][0] == board[1][1] == board[2][2] == 'X':
        user_wins()
    elif board[2][0] == board[1][1] == board[0][2] == 'X':
        user_wins()
    elif board[0][0] == board[0][1] == board[0][2] == 'O':
        computer_wins()
    elif board[1][0] == board[1][1] == board[1][2] == 'O':
        computer_wins()
    elif board[2][0] == board[2][1] == board[2][2] == 'O':
        computer_wins()
    elif board[0][0] == board[1][0] == board[2][0] == 'O':
        computer_wins()
    elif board[1][0] == board[1][1] == board[1][2] == 'O':
        computer_wins()
    elif board[2][0] == board[2][2] == board[2][2] == 'O':
        computer_wins()
    elif board[0][0] == board[1][1] == board[2][2] == 'O':
        computer_wins()
    elif board[2][0] == board[1][1] == board[0][2] == 'O':
        computer_wins()
    else:
        pass


def is_input_valid(marker='None'):
    if marker == 'X':
        return
    else:
        print('Invalid Entry: Enter an X')


def print_board():
    for i in board:
        for j in i:
            print(j, ' ', end='')
        print()


board_empty = True
user_turn = True
wants_to_keep_playing = True
symbol = '*'
board = [
    [symbol, symbol, symbol],
    [symbol, symbol, symbol],
    [symbol, symbol, symbol]
]
'''
print_board()
board[0][0] = 'O'
board[0][1] = 'O'
board[0][2] = 'O'
print_board()
is_game_over()
'''
while wants_to_keep_playing:
    user_turn = True
    while board_empty:
        who_turn = input('Do you want to go first or do you want the Computer to go first? (Me or Computer)')
        if who_turn == 'Me' or who_turn == 'me':
            user_turn = True
        elif who_turn == 'Computer' or who_turn == 'computer':
            user_turn = False
        board_empty = False

    while user_turn:
        print('It is your turn')
        user_mark = input('Enter your Mark: ')
        if user_mark == 'X':
            print_board()
            which_row = int(input('Which Row would you like to place your mark?'))
            which_column = int(input('Which Column would you like to place your mark?'))
            if board[which_row - 1][which_column - 1] == 'X' \
                    or board[which_row - 1][which_column - 1] == 'O':
                print('There is already a marker there. Try Again')
                user_turn = True
            else:
                board[which_row - 1][which_column - 1] = 'X'
                print_board()
                does_someone_win()
                user_turn = False

    while not user_turn:
        print('Computer is taking its turn...')
        which_row = random.randint(0, 3)
        which_column = random.randint(0, 3)
        if board[which_row - 1][which_column - 1] == 'X' \
                or board[which_row - 1][which_column - 1] == 'O':
            user_turn = False
        else:
            board[which_row - 1][which_column - 1] = 'O'
            user_turn = True
            does_someone_win()
            user_turn = True
