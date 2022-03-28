"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if position == 'x' or position == 'o':
        return False
    elif position < 1 or position > 9:
        return False
    return True


def fill_spot(board, position, character):
    character = character.strip().lower()
    board[position - 1] = character


def winning_game(board):
    if board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    return False


def game_over(board):
    if get_winner(board):
        return True
    else:
        x_count = 0
        o_count = 0

        for position in board:
            if position == 'x':
                x_count += 1
            elif position == 'o':
                o_count += 1

        if x_count + o_count == 9:
            return True
        return False


def get_winner(board):
    if winning_game(board):
        x_count = 0
        o_count = 0

        for position in board:
            if position == 'x':
                x_count += 1
            elif position == 'o':
                o_count += 1

        if x_count == o_count:
            return 'o'
        else:
            return 'x'
    else:
        return None


def play(board):
    x_turn = 0
    o_turn = 0
    while not game_over(board):
        print_board(board)
        if x_turn == o_turn:
            position = eval(input("x's, choose a position: "))
            if is_legal(board, position):
                x_turn = x_turn + 1
                fill_spot(board, position, 'x')
        elif x_turn > o_turn:
            position = eval(input("o's, choose a position: "))
            if is_legal(board, position):
                o_turn = o_turn + 1
                fill_spot(board, position, 'o')

    if winning_game(board):
        print(get_winner(board))
    else:
        print('tie')

    play_again = input('do you want to play again? [Y/N] ')
    if play_again == 'y':
        play(build_board())
    else:
        exit()


if __name__ == '__main__':
    play(build_board())
